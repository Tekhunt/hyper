from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import update_session_auth_hash
from api.models.blog import Blog

from api.models.custom_user import User
from api.models.daily_activity import DailyActivity
from api.models.github_issue import GitHubIssue
from api.models.intern_model import Intern
from api.models.pull_request import PullRequest
from api.models.stackoverflow import StackOverflowEngagement
from api.models.twitter_post import TwitterPost
from api.serializers import BlogSerializer, ChangePasswordSerializer, DailyActivitySerializer, GitHubIssueSerializer, InternSerializer, PullRequestSerializer, StackOverflowEngagementSerializer, TwitterPostSerializer, UserSerializer

@extend_schema(tags=["User"])
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(tags=["User"])
class UserListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(tags=["User"])
class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            new_password = serializer.data.get("new_password")

            if not self.object.check_password(old_password):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            self.object.set_password(new_password)
            self.object.save()
            update_session_auth_hash(request, self.object)
            response = {
                "status": status.HTTP_204_NO_CONTENT,
                "message": "Password updated successfully",
            }
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@extend_schema(tags=["Intern"])
class InternListCreateView(generics.ListCreateAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["Intern"])
class InternRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["Blog"])
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["Blog"])
class BlogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["GitHubIssue"])
class GitHubIssueListCreateView(generics.ListCreateAPIView):
    queryset = GitHubIssue.objects.all()
    serializer_class = GitHubIssueSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["GitHubIssue"])
class GitHubIssueRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GitHubIssue.objects.all()
    serializer_class = GitHubIssueSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["PullRequest"])
class PullRequestListCreateView(generics.ListCreateAPIView):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["PullRequest"])
class PullRequestRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["StackOverflow"])
class StackOverflowEngagementListCreateView(generics.ListCreateAPIView):
    queryset = StackOverflowEngagement.objects.all()
    serializer_class = StackOverflowEngagementSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["StackOverflow"])
class StackOverflowEngagementRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StackOverflowEngagement.objects.all()
    serializer_class = StackOverflowEngagementSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["TwitterPost"])
class TwitterPostListCreateView(generics.ListCreateAPIView):
    queryset = TwitterPost.objects.all()
    serializer_class = TwitterPostSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["TwitterPost"])
class TwitterPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TwitterPost.objects.all()
    serializer_class = TwitterPostSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["DailyActivity"])
class DailyActivityListCreateView(generics.ListCreateAPIView):
    queryset = DailyActivity.objects.all()
    serializer_class = DailyActivitySerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["DailyActivity"])
class DailyActivityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyActivity.objects.all()
    serializer_class = DailyActivitySerializer
    permission_classes = [IsAuthenticated]
