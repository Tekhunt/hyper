from django.db import models
from django.conf import settings

class DailyActivity(models.Model):
    DAYS_OF_WEEK = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    ACTIVITY_CHOICES = (
        ('GitHub Pull Request', 'On creating GitHub Pull Request(s)'),
        ('GitHub Issue Solve', 'On solving GitHub Issue(s)'),
        ('GitHub Issue Open', 'On opening GitHub Issue(s)'),
        ('GitHub Issue Comment', 'On commenting GitHub Issue(s)'),
        ('Apache AGE Discord', 'On Apache AGE Discord'),
        ('Meeting', 'On meeting(s)'),
        ('Self Study', 'On Self Study'),
        ('SNS or Blog Posting', 'On posting SNS or blog message(s)'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='daily_activities')
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    date = models.DateField()
    activity = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    activity_duration = models.FloatField()
    activity_description = models.TextField()
    sns_blog_link = models.URLField(max_length=200, blank=True, null=True)
    github_issue_pull_request = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.get_day_of_week_display()}, ({self.date.strftime('%b %d')}) - {self.user.email}"
