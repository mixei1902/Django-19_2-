from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=35, verbose_name='номер телефона', blank=True, null=True,
                             help_text="Введите номер телефона")
    avatar = models.ImageField(upload_to='users/avatars', null=True, blank=True, verbose_name='Аватар',
                               help_text='Загрузите фотографию')
    token = models.CharField(max_length=100, verbose_name='token', blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
