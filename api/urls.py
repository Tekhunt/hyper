from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from api.views import BlogListCreateView, BlogRetrieveUpdateDestroyView, ChangePasswordView, DailyActivityListCreateView, DailyActivityRetrieveUpdateDestroyView, GitHubIssueListCreateView, GitHubIssueRetrieveUpdateDestroyView, InternListCreateView, InternRetrieveUpdateDestroyView, PullRequestListCreateView, PullRequestRetrieveUpdateDestroyView, StackOverflowEngagementListCreateView, StackOverflowEngagementRetrieveUpdateDestroyView, TwitterPostListCreateView, TwitterPostRetrieveUpdateDestroyView, UserCreateAPIView, UserListAPIView, UserRetrieveUpdateDestroyAPIView, WelcomeAPIView


urlpatterns = [
    path("api/v1/welcome/", WelcomeAPIView.as_view(), name='welcome'),
    path("api/v1/usercreate/", UserCreateAPIView.as_view(), name="register"),
    path("api/v1/users/", UserListAPIView.as_view(), name="user-list"),
    path(
        "api/v1/user/<int:pk>/",
        UserRetrieveUpdateDestroyAPIView.as_view(),
        name="single-user",
    ),
    path(
        "api/login/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair_after_login",
    ),
    path("api/change-password/", ChangePasswordView.as_view(), name="change-password"),
    path('api/v1/interns/', InternListCreateView.as_view(), name='intern-list-create'),
    path('api/v1/interns/<int:pk>/', InternRetrieveUpdateDestroyView.as_view(), name='intern-retrieve-update-destroy'),
    path('api/v1/blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('api/v1/blogs/<int:pk>/', BlogRetrieveUpdateDestroyView.as_view(), name='blog-retrieve-update-destroy'),
    path('api/v1/github-issues/', GitHubIssueListCreateView.as_view(), name='github-issue-list-create'),
    path('api/v1/github-issues/<int:pk>/', GitHubIssueRetrieveUpdateDestroyView.as_view(), name='github-issue-retrieve-update-destroy'),
    path('api/v1/pull-requests/', PullRequestListCreateView.as_view(), name='pull-request-list-create'),
    path('api/v1/pull-requests/<int:pk>/', PullRequestRetrieveUpdateDestroyView.as_view(), name='pull-request-retrieve-update-destroy'),
    path('api/v1/stackoverflow-engagements/', StackOverflowEngagementListCreateView.as_view(), name='stackoverflow-engagement-list-create'),
    path('api/v1/stackoverflow-engagements/<int:pk>/', StackOverflowEngagementRetrieveUpdateDestroyView.as_view(), name='stackoverflow-engagement-retrieve-update-destroy'),
    path('api/v1/twitter-posts/', TwitterPostListCreateView.as_view(), name='twitter-post-list-create'),
    path('api/v1/twitter-posts/<int:pk>/', TwitterPostRetrieveUpdateDestroyView.as_view(), name='twitter-post-retrieve-update-destroy'),
     path('api/v1/daily-activities/', DailyActivityListCreateView.as_view(), name='daily-activity-list-create'),
    path('api/v1/daily-activities/<int:pk>/', DailyActivityRetrieveUpdateDestroyView.as_view(), name='daily-activity-retrieve-update-destroy'),
]