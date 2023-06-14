import user.models
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import music.models


class Favorite(models.Model):
    title = models.CharField(max_length=50, default='Избранное', editable=False,
                             verbose_name='название')
    author = models.OneToOneField('user.Profile', on_delete=models.CASCADE, related_name='favorite',
                                  verbose_name='Пользователь')
    music = models.ManyToManyField('music.Music', verbose_name='Музыка')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    @receiver(post_save, sender='user.Profile', dispatch_uid="create_favorite_user")
    def create_favorite(sender, instance, created, **kwargs):
        """Сигнал для создания избранного"""
        if created:
            Favorite.objects.create(author=instance)
        instance.favorite.save()

    def __str__(self) -> str:
        return f'{self.title}, {self.author}'
