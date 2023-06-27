from django.core.exceptions import ValidationError


def validate_music_file(value):
    filesize = value.size

    if filesize > 5024:
        raise ValidationError("You cannot upload file more than 5Mb")
    else:
        return value
