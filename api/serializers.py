from rest_framework import serializers
from api.models.blog import Blog

from api.models.custom_user import User
from api.models.daily_activity import DailyActivity
from api.models.github_issue import GitHubIssue
from api.models.intern_model import Intern
from api.models.pull_request import PullRequest
from api.models.stackoverflow import StackOverflowEngagement
from api.models.twitter_post import TwitterPost


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["old_password", "new_password"]
        extra_kwargs = {
            "old_password": {"write_only": True},
            "new_password": {"write_only": True},
        }


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class GitHubIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitHubIssue
        fields = '__all__'

class PullRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PullRequest
        fields = '__all__'

class StackOverflowEngagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StackOverflowEngagement
        fields = '__all__'

class TwitterPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterPost
        fields = '__all__'

class DailyActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyActivity
        fields = '__all__'

class InternSerializer(serializers.ModelSerializer):
    pull_requests = PullRequestSerializer(many=True, read_only=True, source='user_pull_requests')
    stackoverflow_engagements = StackOverflowEngagementSerializer(many=True, read_only=True, source='user_stackoverflow_engagements')
    blogs = BlogSerializer(many=True, read_only=True, source='user_dev_to_blogs')
    github_issues = GitHubIssueSerializer(many=True, read_only=True, source='user_github_issues')
    twitter_posts = TwitterPostSerializer(many=True, read_only=True, source='user_twitter_posts')

    class Meta:
        model = Intern
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_om",
            "is_intern",
            "profile_image",
        ]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super.update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
