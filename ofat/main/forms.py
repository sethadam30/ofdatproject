from django import forms
from django.forms import ModelForm

from main.models import UserProfile
class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
