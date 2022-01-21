from rest_framework import serializers

from github_scraper.models import GitHubUser, GitHubRepository


class GitHubUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitHubUser
        fields = '__all__'


class GitHubRepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GitHubRepository
        fields = '__all__'


class GitHubUserSimpleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitHubUser
        fields = ['id', 'login', 'name', 'avatar_url', 'synchronized_at']
