from django.test import TestCase

# Create your tests here.
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from main.views import homepage

class HomePageTest(TestCase):
    def test_url_root_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = homepage(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>OFAT</title>', response.content)
        self.assertTrue(response.content.endswith(b'<html>'))
