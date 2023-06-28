from django.core.exceptions import ValidationError
import re


def validate_music_file(value, request):
    filesize = value.size

    if filesize > 500000:
        raise ValidationError("Максимальный размер файла 5Mb")
    else:
        return value


def validate_img(value, request):
    filesize = value.size

    if filesize > 300000:
        raise ValidationError("Максимальный размер файла 3Mb")
    else:
        return value


def validate_password(password):

    if not re.findall('[0-9]', password):
        raise ValidationError("Пароль должен иметь минимум 1 цифру, 0-9.")
    elif not re.findall('[A-Z]', password):
        raise ValidationError(
            "Пароль должен иметь минимум 1 заглавную букву, A-Z")
    elif not re.findall('[a-z]', password):
        raise ValidationError(
            "Пароль должен иметь минимум 1 прописную букву, a-z.")
    elif not re.findall('[@#]', password):
        raise ValidationError(
            "Пароль должен иметь минимум 1 специальный символ: " + "@ or #")
    elif len(password) < 5:
        raise ValidationError("Пароль должен иметь длину минимум 5 символов.")
    return password
