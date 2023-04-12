from django.core.validators import FileExtensionValidator
from django.db import models
from user.models import Profile


class Music(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='автор')
    likes = models.IntegerField(default=0, verbose_name='коллво лайков')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр')
    album = models.ForeignKey('Albums', related_name='musics',  on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/music/', blank=False,
                            verbose_name='Изображение',
                            validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])])
    music_file = models.FileField(upload_to='files/music/',  verbose_name='Файл с музыкой',
                                  validators=[FileExtensionValidator(allowed_extensions=['mp3', ])])

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка'

    def __str__(self) -> str:
        return f'{self.title}, {self.author.username}'


class Genre(models.Model):
    title = models.CharField(max_length=50, verbose_name='название жанра')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f'{self.title}'


class Albums(models.Model):
    title = models.CharField(max_length=50, verbose_name='название альбома')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='исполнитель')
    likes = models.IntegerField(default=0, verbose_name='коллво лайков')
    img = models.ImageField(upload_to='images/albums/', blank=False,
                            verbose_name='Изображение альбома',
                            validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])])

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return f'{self.title}'
