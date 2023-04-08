from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings


class Profile(AbstractUser):
    username = models.CharField(max_length=20, blank=False, null=False, unique=True, default='default_username')
    name = models.CharField(max_length=50, blank=False)
    mobile = models.CharField(max_length=12, unique=True, blank=False)
    address = models.TextField(blank=True, null=True)
    bank_details = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=100, blank=False, default='default_password')

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='user_groups'  # add related name for User model
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='user_permissions'  # add related name for User model
    )

    def __str__(self):
        return f"{self.username} Profile"


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} Profile"


class UserSearch(models.Model):
    user = models.ForeignKey(Profile, related_name='searched_users', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.mobile}, {self.email})"