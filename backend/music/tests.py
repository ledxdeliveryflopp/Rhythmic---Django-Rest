from user.models import Profile
from .models import Music, Genre
from django.test import TestCase


class MusicTest(TestCase):

    def setUp(self):
        self.profile = Profile.objects.create(username='test', password='test', type_user='Исполнитель')
        self.profile.save()
        self.client.login(username='test', password='test')

        self.genre = Genre.objects.create(title='test')
        self.genre.save()

    def test_add_music(self):
        response = self.client.post('/api/create-music/', data={
            'title': 'test',
            'author': 1,
            'genre': 1
        })
        self.assertEqual(response.status_code, 201)

    def test_all_music(self):
        response = self.client.get('/api/all-music/')
        response.json()
        self.assertEqual(response.status_code, 200)
