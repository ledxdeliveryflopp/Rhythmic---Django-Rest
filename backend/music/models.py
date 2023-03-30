from django.core.validators import FileExtensionValidator
from django.db import models
from user.models import Profile


class Music(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    upload_by = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Автор',
                                  blank=False, null=False)
    likes = models.IntegerField(default=0, verbose_name='коллво лайков')

    img = models.ImageField(upload_to='images/music/covers/', blank=False,
                            verbose_name='Изображение',
                            validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])])
    music_file = models.FileField(upload_to='files/tracks/', verbose_name='Файл с музыкой',
                                  validators=[FileExtensionValidator(allowed_extensions=['mp3',
                                                                                         ])])

    CLASSIC = 'Классическая'
    ELECTRONIC = 'Электроника'
    MUSIC_GENRE = (
        (CLASSIC, 'классическая'),
        (ELECTRONIC, 'электроника'),
    )
    genre = models.CharField(max_length=50, verbose_name='Жанр', choices=MUSIC_GENRE)

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка'

    def __str__(self) -> str:
        return f'{self.title}, {self.upload_by.username}'


