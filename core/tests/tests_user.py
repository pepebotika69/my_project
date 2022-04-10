from django.contrib.auth.models import User
from django.test import TestCase


class UserTestCase(TestCase):
    PASSWORD = 'root'
    USERNAME = 'root'
    EMAIL = 'root@root.com'

    def setUp(self):
        user = User.objects.create(username=self.USERNAME, email=self.EMAIL)
        user.set_password(self.PASSWORD)
        user.save()

    def test_user_exists(self):
        users = User.objects.filter(username=self.USERNAME)
        self.assertEqual(1, users.count())
        self.assertTrue(users.exists())

    def test_user_password(self):
        user = User.objects.get(username=self.USERNAME)
        self.assertTrue(user.check_password(self.PASSWORD), 'Password incorrect')

    def test_user_admin_login(self):
        # TODO Это скорее всего пример того как использовать POST запросы, а не тестирование аутентификации
        # С аутентификации надо еще разобраться
        response = self.client.post(
            '/admin/login/',
            {'username': self.USERNAME, 'password': self.PASSWORD},
            follow=True
        )
        self.assertEqual(response.status_code, 200)
