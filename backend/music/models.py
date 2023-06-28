from django.core.validators import FileExtensionValidator
from django.db import models
from album.models import Album
from core.Validators import validate_img, validate_music_file
from user.models import Profile


class Music(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    author = models.ForeignKey(Profile, related_name='musics', on_delete=models.CASCADE,
                               verbose_name='автор')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр')
    album = models.ForeignKey(Album, related_name='musics', on_delete=models.CASCADE,
                              verbose_name='альбом')

    img = models.ImageField(upload_to='music/cover/', blank=False, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg']), validate_img],
                            verbose_name='Изображение')

    music_file = models.FileField(upload_to='files/music/', validators=[FileExtensionValidator(
        allowed_extensions=['mp3', ]), validate_music_file], verbose_name='Файл с музыкой')

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
