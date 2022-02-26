from unicodedata import name
from django.urls import path

from barcode import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('barcode', views.barcode_attendance, name='barcode_attendance'),
    path('mark-barcode-attendance',
         views.mark_barcode_attendance, name='mark-attendance'),
    path('finger-print', views.finger_print_scanner,
         name='finger-print_attendance')
]
