from django.db import models


# Create your models here.
class GitHubUser(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    login = models.CharField(blank=True, max_length=100, null=True)
    avatar_url = models.URLField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    html_url = models.URLField(blank=True, null=True)
    site_admin = models.BooleanField()
    name = models.CharField(blank=True, null=True, max_length=200)
    company = models.CharField(blank=True, null=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    synchronized_at = models.DateTimeField()


class GitHubRepository(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    user = models.ForeignKey(GitHubUser, on_delete=models.PROTECT, related_name='repositories')
    full_name = models.CharField(max_length=500)
    html_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    pushed_at = models.DateTimeField()
