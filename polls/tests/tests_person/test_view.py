import uuid     # noqa: F401

from django.test import TestCase
from django.urls import reverse

from polls.models import Person


class PersonListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_persons = 13

        for person_id in range(number_of_persons):
            Person.objects.create(
                first_name=f'Some Name {person_id}',
                last_name=f'Some Surname {person_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/polls/persons/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('polls:persons'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('polls:persons'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/person_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('polls:persons'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'], True)
        self.assertEqual(len(response.context['person_list']), 10)

    def test_lists_all_persons(self):
        response = self.client.get(reverse('polls:persons') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'], True)
        self.assertEqual(len(response.context['person_list']), 3)


class PersonDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Person.objects.create(
            first_name='Some Name',
            last_name='Some Surname'
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/polls/person/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('polls:person-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('polls:persons'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/person_list.html')

    # def test_HTTP404_for_invalid_person(self):
    #     test_uid = uuid.uuid4()
    #     response = self.client.get(reverse('polls:person-detail', kwargs={'pk': test_uid}))
    #     self.assertEqual(response.status_code, 404)


class PersonCreateTest(TestCase):
    def setUp(self):
        test_person = Person.objects.create(first_name='Some Name', last_name='Some Surname')       # noqa: F841

    def test_uses_correct_template(self):
        response = self.client.get(reverse('polls:person-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/person_form.html')

    def test_redirects_to_detail_view_on_success(self):
        response = self.client.post(reverse('polls:person-create'),
                                    {'first_name': 'Some Name', 'last_name': 'Some Surname'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/polls/persons/'))


class PersonUpdateTest(TestCase):
    def setUp(self):
        test_person = Person.objects.create(first_name='Some Name', last_name='Some Surname')           # noqa: F841

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('polls:person-update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get(reverse('polls:person-update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/person_form.html')

    def test_redirects_to_all_persons_on_success(self):
        response = self.client.post(reverse('polls:person-update', kwargs={'pk': 1}),
                                    {'first_name': 'Some Name', 'last_name': 'Some Surname'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/polls/persons/'))

    # def test_HTTP404_for_invalid_person(self):
    #     test_uid = uuid.uuid4()
    #     response = self.client.get(reverse('polls:person-update', kwargs={'pk': test_uid}))
    #     self.assertEqual(response.status_code, 404)
