from django.urls import path

from barcode import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
]
