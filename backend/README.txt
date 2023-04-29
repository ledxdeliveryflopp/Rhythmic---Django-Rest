api/ - главная ссылка на api

Приложение music

all-music/ - ссылка на весь список музыки
create-music/ - ссылка на создание музыки
music<int:pk>/ - ссылка на прослушивание музыки
update-music<id>/ - ссылка на изменение музыки

Приложение user

all/ - ссылка на весь список юзеров
user<id>/ - ссылка на юзера с опеределенным id
register/ - ссылка на регистрацию
update-user<id> - ссылка на изменение юзера
login/ - ссылка на вход
logaut/ - ссылка на выход с удалением токена


docker compose up -d --build

python manage.py makemigrations
python manage.py migrate user
python manage.py migrate knox
python manage.py migrate session
python manage.py migrate music
python manage.py migrate album
python manage.py migratedocker