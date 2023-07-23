from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from api.models.user_manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("first name"), max_length=255, blank=True, null=True)
    last_name = models.CharField(_("last name"), max_length=255, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True)
    profile_image = models.URLField(blank=True, null=True)
    # New fields to differentiate between OM and intern
    is_om = models.BooleanField(default=False)
    is_intern = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
