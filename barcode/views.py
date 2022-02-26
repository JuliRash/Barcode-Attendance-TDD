from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

from barcode.models import Attendance, Person, Setup
from barcode.decorators import setup_is_configured


@setup_is_configured
def home_page(request):
    setup = Setup.objects.first()
    context = {'setup': setup}
    return render(request, 'home.html', context)


@setup_is_configured
def barcode_attendance(request):
    setup = Setup.objects.first()
    today_date = date.today()
    if request.method == 'POST':
        try:
            person = Person.objects.get(code=request.POST['code'])
            attendance = Attendance.objects.save_attendance(
                person=person, date=today_date.day)
            context = {'attendance': attendance, 'setup': setup}
        except Person.DoesNotExist:
            context = {
                'error': 'Error: This user does not exist.', 'setup': setup}
        return render(request, 'home.html', context)
    context = {'setup': setup}
    # return render(request, 'home.html', context)
    return render(request, 'barcode.html', context)


@setup_is_configured
def mark_barcode_attendance(request):
    setup = Setup.objects.first()
    today_date = date.today()
    if request.method == 'POST':
        try:
            person = Person.objects.get(code=request.POST['code'])
            attendance = Attendance.objects.save_attendance(
                person=person, date=today_date.day)
            context = {'attendance': attendance, 'setup': setup}
        except Person.DoesNotExist:
            context = {
                'error': 'Error: This user does not exist.', 'setup': setup}
        return render(request, 'marked-attendance.html', context)


@setup_is_configured
def finger_print_scanner(request):
    return HttpResponse('Work in Progress')
