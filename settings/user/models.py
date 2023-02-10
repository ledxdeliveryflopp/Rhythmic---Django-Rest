from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from rest_framework.authtoken.models import Token


class Profile(AbstractUser):
    # USER_TYPE_CHOICES = (
    #     (1, 'Обычный пользователь'),
    #     (2, 'Исполнитель'),
    # )

    type_user = models.BooleanField(verbose_name='Исполнитель?', default=False)
    img = models.ImageField(upload_to='images/user/avatars/', null=True, blank=True,
                            verbose_name='Аватар',
                            validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


