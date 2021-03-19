from django.test import TestCase
from django.urls import resolve
from django.template.loader import render_to_string

from barcode.views import home_page


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_post_request(self):
        response = self.client.post('/', data={'id_number': '0909'})
        self.assertIn('0909', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
