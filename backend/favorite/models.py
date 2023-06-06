from django.db import models
from music.models import Music
from user.models import Profile


class Favorite(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE,
                               verbose_name='автор')
    music = models.ManyToManyField(Music, blank=True, verbose_name='Избранное')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        return f'{self.author}'

