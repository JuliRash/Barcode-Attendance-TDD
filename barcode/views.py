from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    if request.method == 'POST':
        return render(request, 'home.html', {'id_number': request.POST['id_number'],})
    return render(request, 'home.html')
