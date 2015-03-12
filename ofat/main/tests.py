from django.test import TestCase

# Create your tests here.
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.http import HttpRequest
from main.views import homepage
import os
from main.models import UserProfile

class HomePageTest(TestCase):
    def test_url_root_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = homepage(request)
        expected_html = render_to_string('main/home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['username'] = 'Test user'

        response = homepage(request)
        self.assertIn('Registration was succesful',response.content.decode())
        
    def test_bootstrap_available(self):
        self.assertTrue(os.path.exists('static/css/bootstrap.min.css'))

class UserProfileModelTest(TestCase):
    def test_saving_and_retrieving_profiles(self):
        from django.contrib.auth.models import User
        u1 = User()
        u1.username = 'user1'
        u1.save()

        u2 = User()
        u2.username = 'user2'
        u2.save()
                
        profile1 = UserProfile()
        profile1.user = u1
        profile1.email = 'test@user.com'
        profile1.save()

        profile2 = UserProfile()
        profile2.user = u2
        profile2.email = 'test@user2.com'
        profile2.save()

        saved_profiles = UserProfile.objects.all()
        self.assertEqual(saved_profiles.count(), 2)

        first_saved_profile = saved_profiles[0]
        second_saved_profile = saved_profiles[1]
        self.assertEqual(first_saved_profile.email, 'test@user.com')
        self.assertEqual(second_saved_profile.email, 'test@user2.com')
