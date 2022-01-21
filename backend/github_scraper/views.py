from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework import permissions

from backend.tasks import fetch_data
from github_scraper.models import GitHubUser, GitHubRepository
from github_scraper.serializers import GitHubUserSimpleListSerializer, GitHubRepositorySerializer

class DashboardGitHubView(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'])
    def github_user_list(self, request):
        github_user = GitHubUser.objects.all()
        github_user_serializer = GitHubUserSimpleListSerializer(instance=github_user, many=True)
        return Response(github_user_serializer.data)

    @action(detail=False, methods=['get'])
    def github_user_repositories(self, request):
        user_id = self.request.GET.get('user_id', None)
        github_repositories = GitHubRepository.objects.filter(user_id=user_id).all()
        github_repositories_serializer = GitHubRepositorySerializer(instance=github_repositories, many=True)
        return Response(github_repositories_serializer.data)

    @action(detail=False, methods=['post'])
    def cron_query(self, request):
        username = self.request.data.get('username', None)
        countdown = int(self.request.data.get('countdown', 5))
        fetch_data.s(username).apply_async(countdown=countdown)
        return Response(status=HTTP_200_OK)
