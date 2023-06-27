from django.test import TestCase
from .models import Profile


class RegisterTestUser(TestCase):

    def setUpUser(self):
        self.user = Profile.objects.create(username='test', password='test', type_user='Исполнитель')
        self.user.save()
        self.client.login(username='test', password='test')

    def test_all_user(self):
        response = self.client.get('/api/all/')
        response.json()
        self.assertEqual(response.status_code, 200)
