from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    from django.contrib.auth.forms import UserCreationForm
    from main.forms import UserProfileForm

    registered = False
    uform = UserCreationForm()
    pform = UserProfileForm()
    if request.method == 'POST':
        uform = UserCreationForm(request.POST)
        pform = UserProfileForm(request.POST)
        if uform.is_valid() and pform.is_valid():
            new_user = uform.save()
            pform.instance.user = new_user
            pform.save()
            return redirect('/?registration=success')

    if request.method == 'GET' and 'registration' in request.GET:
        registered = True
    
    return render(request, 'main/home.html',
                  {'userform': uform,
                   'profileform': pform,
                   'registered': registered})
