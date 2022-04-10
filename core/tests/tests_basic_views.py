from django.contrib.auth.models import User
from django.test import TestCase


class BasicViewsTestCase(TestCase):
    PASSWORD = 'root'
    USERNAME = 'root'
    EMAIL = 'root@root.com'

    def setUp(self):
        user = User.objects.create(username=self.USERNAME, email=self.EMAIL)
        user.set_password(self.PASSWORD)
        user.save()

    def test_user_is_forbidden(self):
        response = self.client.get('/core/asyncio/')
        self.assertEqual(response.status_code, 403)
