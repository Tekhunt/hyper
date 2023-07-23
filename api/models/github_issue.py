from django.db import models
from django.conf import settings

class GitHubIssue(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='github_issues')
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
