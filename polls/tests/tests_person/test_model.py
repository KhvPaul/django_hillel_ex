from django.test import TestCase

from polls.models import Person


class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Person.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_first_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 150)

    def test_last_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_last_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 150)

    def test_email_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email address')

    def test_object_name_is_last_name_plus_first_name(self):
        person = Person.objects.get(id=1)
        expected_object_name = f'{person.last_name}, {person.first_name}'
        self.assertEqual(str(person), expected_object_name)

    def test_get_absolute_url(self):
        person = Person.objects.get(id=1)
        self.assertEqual(person.get_absolute_url(), '/polls/person/1')
