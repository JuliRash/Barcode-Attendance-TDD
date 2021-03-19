from django.test import TestCase

from barcode.models import Attendance, Person


class AttendanceModelTest(TestCase):

    def test_saving_and_retrieving_user_attendance(self):
        first_person = Person.objects.create(
            first_name='julipels',
            last_name='idowu',
            other_name='ropee',
            email='idowujulius92@gmail.com',
            id_number='0909')

        second_person = Person.objects.create(
            first_name='julipels',
            last_name='idowu',
            other_name='ropee',
            email='idowujulius92@gmail.com',
            id_number='0908')

        first_attendance = Attendance()
        first_attendance.person = first_person
        first_attendance.date = '2021-02-09'
        first_attendance.time_in = '13:44:48'
        first_attendance.time_out = '13:44:48'
        first_attendance.purpose = 'Christening'
        first_attendance.location = 'Delta-Side'
        first_attendance.save()

        second_attendance = Attendance()

        second_attendance.person = second_person
        second_attendance.date = '2021-02-09'
        second_attendance.time_in = '13:44:48'
        second_attendance.time_out = '13:44:48'
        second_attendance.purpose = 'Christening'
        first_attendance.location = 'Alpha-side'
        second_attendance.save()

        saved_attendances = Attendance.objects.all()

        first_saved_attendance = saved_attendances[0]
        second_saved_attendance = saved_attendances[1]

        self.assertEqual(saved_attendances.count(), 2)
        self.assertEqual(first_saved_attendance.person.id_number, '0909')
        self.assertEqual(second_saved_attendance.person.id_number, '0908')
