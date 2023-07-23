from django.db import models
from django.conf import settings

class OperationalManager(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    discordID = models.CharField(max_length=50)
    dev_to_url = models.URLField(max_length=200)
    email = models.EmailField()
    github = models.URLField(max_length=200)
    stackoverflow_url = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"