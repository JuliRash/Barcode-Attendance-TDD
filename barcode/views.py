from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse('<html><title>Barcode Attendance</title><<h1>Barcode Attendance</h1></html>')
