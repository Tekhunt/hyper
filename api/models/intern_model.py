from django.db import models
from django.conf import settings
from api.models.om_model import OperationalManager

class Intern(models.Model):
    YEAR_OPTIONS = (
        ('Year 1', 'Year 1'),
        ('Year 2', 'Year 2'),
        ('Year 3', 'Year 3'),
        ('Year 4', 'Year 4'),
        ('Year 5', 'Year 5'),
        ('PassedOut', 'PassedOut'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    operational_manager = models.OneToOneField(OperationalManager, on_delete=models.CASCADE, related_name='intern')
    discordID = models.CharField(max_length=50)
    dev_to_url = models.URLField(max_length=200)
    email = models.EmailField()
    github = models.URLField(max_length=200)
    stackoverflow_url = models.URLField(max_length=200)
    year_in_college = models.CharField(max_length=10, choices=YEAR_OPTIONS)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"