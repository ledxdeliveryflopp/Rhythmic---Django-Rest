from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from core.Validators import validate_img


class Profile(AbstractUser):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='id')
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
                                                                                   'jpeg']),
                                        validate_img])


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f'{self.username}, {self.type_user}'
