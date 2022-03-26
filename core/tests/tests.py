from django.test import TestCase

from core.models import Animal


class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name_female="кошка", name_male="кот")

    def test_animals_name(self):
        cat = Animal.objects.get(name_male="кот")
        self.assertEqual(cat.name_female, 'кошка')
        self.assertEqual(cat.name_male, 'кот')
