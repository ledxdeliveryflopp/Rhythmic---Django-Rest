from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models

#TODO: сделать минимальные требования для пароля


class Profile(AbstractUser):
    SINGER = 'Исполнитель'
    STANDARD = 'Стандартный'
    USER_STATUS = (
        (SINGER, 'Исполнитель'),
        (STANDARD, 'Стандартный'),
    )
    type_user = models.CharField(max_length=30, choices=USER_STATUS, verbose_name='Тип профиля')
    img = models.ImageField(upload_to='user/avatars/', null=False, blank=False,
                            verbose_name='Аватар',
                            validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg',
                                                                                   'jpeg'])])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f'{self.username}, {self.type_user}'

