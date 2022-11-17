import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(
        verbose_name='id',
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    email = models.EmailField(
        verbose_name='email',
        unique=True,
        blank=False,
        null=True
    )
    profile_img = models.ImageField(
        verbose_name='Profile Picture',
        null=True,
        blank=True,
        default='User.png'
    )

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
