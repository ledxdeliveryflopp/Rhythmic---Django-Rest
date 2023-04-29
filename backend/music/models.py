from django.core.validators import FileExtensionValidator
from django.db import models
from album.models import Album
from playlist.models import Playlist
from user.models import Profile


class Music(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    author = models.ForeignKey(Profile, related_name='musics', on_delete=models.CASCADE,
                               verbose_name='автор')
    likes = models.ManyToManyField('Like', related_name='likes', verbose_name='коллво лайков')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр')
    album = models.ForeignKey(Album, related_name='musics', on_delete=models.CASCADE,
                              verbose_name='альбом')
    playlist = models.ForeignKey(Playlist, related_name='musics', on_delete=models.CASCADE,
                                 verbose_name='плейлист', null=True, blank=True)

    img = models.ImageField(upload_to='images/music/', blank=False, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg'])], verbose_name='Изображение')

    music_file = models.FileField(upload_to='files/music/', validators=[FileExtensionValidator(
        allowed_extensions=['mp3', ])], verbose_name='Файл с музыкой')

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка'

    def __str__(self) -> str:
        return f'{self.title}, {self.author.username}'


class Like(models.Model):
    title = models.ManyToManyField(Profile)

    def __str__(self):
        return f'{self.title}'


class Genre(models.Model):
    title = models.CharField(max_length=50, verbose_name='название жанра')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f'{self.title}'
