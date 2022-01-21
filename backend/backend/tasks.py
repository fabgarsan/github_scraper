import json

import requests
from django.utils import timezone

from github_scraper.models import GitHubUser, GitHubRepository
from github_scraper.serializers import GitHubUserSerializer, GitHubRepositorySerializer
from .celery import app

import socketio

sio = socketio.Client()


@app.task
def fetch_data(username):
    response_user = requests.get(f"https://api.github.com/users/{username}")
    data = json.loads(response_user.content.decode())
    data['synchronized_at'] = timezone.now()
    user_id = data.get('id', None)

    if user_id:
        users_by_id = GitHubUser.objects.filter(id=user_id)
        if not users_by_id.exists():
            new_user_serializer = GitHubUserSerializer(data=data)
            new_user_serializer.is_valid(raise_exception=True)
            new_user_serializer.save()
        else:
            founded_user_serializer = GitHubUserSerializer(users_by_id.first(), data=data, partial=True)
            founded_user_serializer.is_valid(raise_exception=True)
            founded_user_serializer.save()
        response_repositories = requests.get(f"https://api.github.com/users/{username}/repos")
        data = json.loads(response_repositories.content.decode())
        for repository_data in data:
            repository_id = repository_data.get('id', None)
            repositories_by_id = GitHubRepository.objects.filter(id=repository_id)
            if not repositories_by_id.exists():
                repository_data['user'] = user_id
                new_repository_serializer = GitHubRepositorySerializer(data=repository_data)
                new_repository_serializer.is_valid(raise_exception=True)
                new_repository_serializer.save()
            else:
                founded_repository_serializer = GitHubRepositorySerializer(
                    repositories_by_id.first(),
                    data=repository_data,
                    partial=True
                )
                founded_repository_serializer.is_valid(raise_exception=True)
                founded_repository_serializer.save()
        if not sio.connected:
            sio.connect('ws://sockets:3000')
        sio.emit('chat message', f"Synchronize {username}")
