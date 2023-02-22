FROM python:3.12-rc-slim-buster

WORKDIR /settings

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ['python', 'manage.py', 'runserver']