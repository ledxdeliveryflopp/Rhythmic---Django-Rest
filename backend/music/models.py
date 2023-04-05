from django.core.validators import FileExtensionValidator
from django.db import models
from user.models import Profile


class Music(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='автор')
    likes = models.IntegerField(default=0, verbose_name='коллво лайков')
    album = models.ForeignKey('Album', on_delete=models.CASCADE, null=True, verbose_name='альбом')

    img = models.ImageField(upload_to='images/music/covers/', blank=False,
                            verbose_name='Изображение',
                            validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])])
    music_file = models.FileField(upload_to='files/tracks/', verbose_name='Файл с музыкой',
                                  validators=[FileExtensionValidator(allowed_extensions=['mp3', ])])


    CLASSIC = 'Классическая'
    ELECTRONIC = 'Электроника'
    ROCK = 'Рок'
    ALTERNATIVE = 'Альтернатива'
    DRUMANDBASS = 'Драм-н-бейс'
    DABSTEP = 'Дабстеп'
    RUSSIANROCK = 'Русский рок'
    POP = 'Поп'
    NUMETAL = 'Ню-метал'
    METAL = 'Метал'
    MUSIC_GENRE = (
        (CLASSIC, 'классическая'),
        (ELECTRONIC, 'электроника'),
        (ALTERNATIVE, 'Альтернатива'),
        (DRUMANDBASS, 'Драм-н-бейс'),
        (DABSTEP, 'Дабстеп'),
        (RUSSIANROCK, 'Русский рок'),
        (POP, 'Поп'),
        (NUMETAL, 'Ню-метал'),
        (METAL, 'Метал'),
    )
    genre = models.CharField(max_length=50, verbose_name='Жанр', choices=MUSIC_GENRE)

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка'

    def __str__(self) -> str:
        return f'{self.title}, {self.author.username}'


class Album(models.Model):
    title = models.CharField(max_length=50, verbose_name='название альбома')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='исполнитель')
    tracks = models.ManyToManyField(Music, verbose_name='трэки', related_name='+')
    likes = models.IntegerField(default=0, verbose_name='коллво лайков')
    img = models.ImageField(upload_to='images/albums/covers/', blank=False,
                            verbose_name='Изображение альбома',
                            validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])])

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return f'{self.title}'
