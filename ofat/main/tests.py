from django.test import TestCase

# Create your tests here.
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.http import HttpRequest
from main.views import homepage
import os

class HomePageTest(TestCase):
    def test_url_root_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = homepage(request)
        expected_html = render_to_string('main/home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_bootstrap_available(self):
        self.assertTrue(os.path.exists('static/css/bootstrap.min.css'))
        
