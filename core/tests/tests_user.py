from django.test import TestCase

from django.contrib.auth.models import User


class AnimalTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="root", email='root@root.com')
        user.set_password('root')
        user.save()

    def test_animals_name(self):
        users = User.objects.filter(username="root")
        self.assertEqual(1, users.count())
