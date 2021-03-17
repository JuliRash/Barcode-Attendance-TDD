from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from barcode.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home_page)

