from django.core.validators import FileExtensionValidator
from django.db import models
from user.models import Profile


class Album(models.Model):
    title = models.CharField(max_length=50, verbose_name='название альбома')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE,
                               verbose_name='исполнитель')
    img = models.ImageField(upload_to='album/cover/', blank=False,
                            validators=[FileExtensionValidator(allowed_extensions=['png',
                                                                                   'jpg', 'jpeg'])],
                            verbose_name='Изображение альбома',)

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return f'{self.title}'
