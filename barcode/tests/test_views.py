from django.test import TestCase

from barcode.models import Attendance, Person


class HomePageTest(TestCase):

    def setUp(self):
        person = Person.objects.create(
            first_name='julipels',
            last_name='idowu',
            other_name='ropee',
            email='idowujulius92@gmail.com',
            id_number='0909')

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_post_request(self):
        self.client.post('/', data={'id_number': '0909'})
        self.assertEqual(Attendance.objects.count(), 1)
        new_attendance = Attendance.objects.first()
        self.assertEqual(new_attendance.person.id_number, '0909')

    def test_returns_ok_after_POST(self):
        response = self.client.post('/', data={'id_number': '0909'})
        self.assertEqual(response.status_code, 200)

    def test_displays_user_info(self):
        response = self.client.post('/', data={'id_number': '0909'})
        self.assertIn('julipels', response.content.decode())

