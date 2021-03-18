from django.test import TestCase
from django.urls import resolve
from django.template.loader import render_to_string

from barcode.views import home_page


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
