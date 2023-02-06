from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Обычный пользователь'),
        (2, 'Исполнитель'),
    )

    type_user = models.IntegerField(verbose_name='Тип профиля'
                                                 , choices=USER_TYPE_CHOICES, default=1)
    img = models.ImageField(upload_to='images/user/avatars/', null=True, blank=True,
                            verbose_name='Аватар')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


