from django.db import models
from user.models import Profile


class Playlist(models.Model):
    title = models.CharField(max_length=50, verbose_name='название плейлиста')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE,
                               verbose_name='автор')

    class Meta:
        verbose_name = 'плейлист'
        verbose_name_plural = 'плейлисты'

    def __str__(self):
        return f'{self.title}'
