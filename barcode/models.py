from django.db import models
from datetime import datetime


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, )
    other_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.id_number


class Attendance(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    time_in = models.TimeField(default=datetime.now)
    time_out = models.TimeField(blank=True, default=datetime.now)
    purpose = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, default='Barcode Attendance')

    def __Str__(self):
        return self.person
