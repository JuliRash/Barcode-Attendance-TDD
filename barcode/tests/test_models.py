from django.test import TestCase

from barcode.models import Attendance, Person, Setup


def generate_demo_person_data(user_code):
    return Person.objects.create(first_name='julipels',
                                 last_name='idowu',
                                 other_name='ropee',
                                 email='idowujulius92@gmail.com',
                                 code=user_code)


def generate_demo_setup_data():
    return Setup.objects.create(organization_name='Ropee Inc', organization_location='Nigeria')


class AttendanceModelTest(TestCase):

    def test_saving_and_retrieving_user_attendance(self):
        first_person = generate_demo_person_data('0909')
        second_person = generate_demo_person_data('0908')

        Attendance.objects.bulk_create([Attendance(person=first_person,
                                                   date='2021-02-09',
                                                   time_in='13:44:48',
                                                   time_out='13:44:48',
                                                   purpose='Christening',
                                                   location='Alpha-side'),
                                        Attendance(person=second_person,
                                                   date='2021-02-09',
                                                   time_in='13:44:48',
                                                   time_out='13:44:48',
                                                   purpose='Christening',
                                                   location='Alpha-side'), ])

        saved_attendances = Attendance.objects.all()

        first_saved_attendance = saved_attendances[0]
        second_saved_attendance = saved_attendances[1]

        self.assertEqual(saved_attendances.count(), 2)
        self.assertEqual(first_saved_attendance.person.code, '0909')
        self.assertEqual(second_saved_attendance.person.code, '0908')
