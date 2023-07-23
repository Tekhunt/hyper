from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from api.views import ChangePasswordView, UserCreateAPIView, UserListAPIView, UserRetrieveUpdateDestroyAPIView


urlpatterns = [
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
]