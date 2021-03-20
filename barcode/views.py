from django.shortcuts import redirect, render
from django.http import HttpResponse

from barcode.models import Attendance, Person


def home_page(request):
    if request.method == 'POST':
        user_id_number = Person.objects.filter(id_number=request.POST['id_number'])
        if user_id_number.exists():
            attendance = Attendance.objects.create(person=user_id_number.get())
            return render(request, 'home.html', {'attendance': attendance})
        else:
            return render(request, 'home.html', {'error': 'Error: This user does not exist'})
    return render(request, 'home.html')
