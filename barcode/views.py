from django.shortcuts import redirect, render
from django.http import HttpResponse

from barcode.models import Attendance, Person
from barcode.decorators import setup_is_configured


@setup_is_configured
def home_page(request):
    if request.method == 'POST':
        try:
            person = Person.objects.get(code=request.POST['code'])
            attendance = Attendance.objects.create(person=person)
            context = {'attendance': attendance}
        except Person.DoesNotExist:
            context = {'error': 'Error: This user does not exist.'}
        return render(request, 'home.html', context)
    return render(request, 'home.html')
