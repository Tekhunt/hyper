from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import update_session_auth_hash

from api.models.custom_user import User
from api.serializers import ChangePasswordSerializer, UserSerializer

@extend_schema(tags=["Users"])
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(tags=["Users"])
class UserListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(tags=["Users"])
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

