from django.shortcuts import render
from datetime import date

from barcode.models import Attendance, Person, Setup
from barcode.decorators import setup_is_configured


@setup_is_configured
def home_page(request):
    setup = Setup.objects.first()
    today_date = date.today()
    if request.method == 'POST':
        try:
            person = Person.objects.get(code=request.POST['code'])
            attendance = Attendance.objects.save_attendance(person=person, date=today_date.day)
            context = {'attendance': attendance, 'setup': setup}
        except Person.DoesNotExist:
            context = {'error': 'Error: This user does not exist.', 'setup': setup}
        return render(request, 'home.html', context)
    context = {'setup': setup}
    return render(request, 'home.html', context)
