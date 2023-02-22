# Generated by Django 4.1.6 on 2023-02-20 17:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0004_remove_music_genre_remove_music_upload_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='коллво лайков'),
        ),
        migrations.AlterField(
            model_name='music',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.genre', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='music',
            name='img',
            field=models.ImageField(upload_to='images/music/covers/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg'])], verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='music',
            name='music_file',
            field=models.FileField(upload_to='files/tracks/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3'])], verbose_name='Файл с музыкой'),
        ),
        migrations.AlterField(
            model_name='music',
            name='upload_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
