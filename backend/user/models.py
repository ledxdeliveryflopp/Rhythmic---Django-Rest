from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import validate_password
from django.core.validators import FileExtensionValidator
from django.db import models

from .validators import NumberValidator, SymbolValidator


class Profile(AbstractUser):
    SINGER = 'Исполнитель'
    STANDARD = 'Стандартный'
    USER_STATUS = (
        (SINGER, 'Исполнитель'),
        (STANDARD, 'Стандартный'),
    )

    type_user = models.CharField(max_length=30, choices=USER_STATUS)
    type = models.BooleanField(verbose_name='Исполнитель?', default=False)
    img = models.ImageField(upload_to='images/user/avatars/', null=True, blank=True,
                            verbose_name='Аватар',
                            validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f'{self.username}, {self.type_user}'


