from django.core.validators import FileExtensionValidator
from django.db import models
from user.models import Profile


class Albums(models.Model):
    title = models.CharField(max_length=50, verbose_name='название альбома')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='исполнитель')
    likes = models.IntegerField(default=0, verbose_name='коллво лайков')
    img = models.ImageField(upload_to='images/albums/', blank=False,
                            validators=[FileExtensionValidator(allowed_extensions=['png',
                                                                                   'jpg'])],
                            verbose_name='Изображение альбома',)

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return f'{self.title}'
