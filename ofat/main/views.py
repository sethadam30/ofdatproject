from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    from django.contrib.auth.forms import UserCreationForm
    from main.forms import UserProfileForm

    registered = False
    if request.method == 'POST':
        return redirect('/?registration=success')

        if request.method == 'GET' and request.GET['registration'] == 'success':
            registered = True
    
    return render(request, 'main/home.html',
                  {'userform': UserCreationForm(),
                   'profileform': UserProfileForm(),
                   'registered': registered})
