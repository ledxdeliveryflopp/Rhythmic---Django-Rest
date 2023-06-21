from django.test import TestCase
from user.models import Profile


class AlbumTest(TestCase):

    def setUp(self):
        self.profile = Profile.objects.create(username='test', password='test', type_user='Исполнитель')
        self.profile.save()
        self.client.login(username='test', password='test')

    def test_add_album(self):
        response = self.client.post('/api/create-album/', data={
            'title': 'test',
            'author': 1,
        })
        self.assertEqual(response.status_code, 201)

    def test_all_music(self):
        response = self.client.get('/api/all-album/')
        response.json()
        self.assertEqual(response.status_code, 200)
