from django.core.validators import FileExtensionValidator
from django.db import models
from music.models import Music
from user.models import Profile


class Playlist(models.Model):
    title = models.CharField(max_length=50, verbose_name='название плейлиста')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE,
                               verbose_name='автор')
    music = models.ManyToManyField(Music, verbose_name='музыка', blank=True)

    img = models.ImageField(upload_to='playlist/cover/', blank=False, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])],
                            verbose_name='Изображение')

    class Meta:
        verbose_name = 'плейлист'
        verbose_name_plural = 'плейлисты'

    def __str__(self):
        return f'{self.title}'
