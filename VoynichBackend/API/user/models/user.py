import logging

from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager)
from django.db import models

logger = logging.getLogger(__name__)


class User(AbstractBaseUser, PermissionsMixin):
    auth_id = models.CharField(max_length=255, editable=False)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    avatar_cropped = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        app_label = 'user'

    def __str__(self):
        return self.username
