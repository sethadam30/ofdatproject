from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    from django.contrib.auth.forms import UserCreationForm
    from main.forms import UserProfileForm

    registered = False
    if request.method == 'POST':
        registered = True
    
    return render(request, 'main/home.html',
                  {'userform': UserCreationForm(),
                   'profileform': UserProfileForm(),
                   'registered': registered})
