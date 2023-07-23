from rest_framework import serializers

from api.models.custom_user import User


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
