from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

class TestPortalCheckin(APITestCase):

    base_url = '/example/'

    def setUp(self):
        user = User.objects.create_superuser('admin', 'admin@admin.com', 'adminadmin')
        token = Token(user=user)
        token.save()
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + token.key
        )

    def test_create_widget(self):
        data = {'name': 'testing', 'description': 'testing'}
        res = self.client.post(self.base_url, data, format='json')
        assert res.status_code == 201
