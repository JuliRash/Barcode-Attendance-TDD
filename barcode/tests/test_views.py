from django.test import TestCase

from barcode.models import Attendance, Person
from barcode.tests.test_models import generate_demo_setup_data


class HomePageTest(TestCase):

    def setUp(self):
        person = Person.objects.create(
            first_name='julipels',
            last_name='idowu',
            other_name='ropee',
            email='idowujulius92@gmail.com',
            code='0909')
        setup_configuration = generate_demo_setup_data()

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_post_request(self):
        self.client.post('/', data={'code': '0909'})
        self.assertEqual(Attendance.objects.count(), 1)
        new_attendance = Attendance.objects.first()
        self.assertEqual(new_attendance.person.code, '0909')

    def test_returns_ok_after_POST(self):
        response = self.client.post('/', data={'code': '0909'})
        self.assertEqual(response.status_code, 200)

    def test_displays_user_info_if_successful(self):
        response = self.client.post('/', data={'code': '0909'})
        self.assertIn('julipels', response.content.decode())

    def test_displays_error_to_user_if_unsuccessful(self):
        response = self.client.post('/', data={'code': '0908'})
        self.assertIn('Error', response.content.decode())

