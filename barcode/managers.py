from django.db import models
from datetime import datetime


class AttendanceManager(models.Manager):
    """
    Custom Manager for Attendance
    """
    def save_attendance(self, person, date):
        attendance = self.filter(person=person, date__day=date, time_out__isnull=True)
        if not attendance:
            return self.create(person=person)
        else:
            for obj in attendance:
                obj.time_out = datetime.now().time()
                obj.save()
                return obj
