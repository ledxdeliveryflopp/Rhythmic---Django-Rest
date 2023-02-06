from django.core.validators import FileExtensionValidator
from django.db import models
from user.models import Profile


class Music(models.Model):
    title = models.CharField(max_length=50, unique=True)
    upload_by = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Автор',
                                  blank=False, null=False)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр', blank=False,
                              null=False)

    img = models.ImageField(upload_to='images/music/covers/', blank=False,
                            verbose_name='Изображение')
    music_file = models.FileField(upload_to='files/tracks/', verbose_name='Файл с музыкой',
                                  validators=[FileExtensionValidator(allowed_extensions=['mp3', ])])

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка'

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименования', unique=True, null=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.title

