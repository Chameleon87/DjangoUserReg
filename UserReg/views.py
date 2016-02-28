from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from UserReg.forms import RegistrationForm

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'accounts/login.html')

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return render(request, 'accounts/user_profile.html')
    else:
        return HttpResponseRedirect('accounts/invalid')

def invalid_login():
    return render_to_response('accounts/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'accounts/logout.html')

def register_user(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/user_profile.html')
        else:
            return render(request, 'accounts/register.html',
                          {"form" : form})
    else:
        return render(request, 'accounts/register.html',
                      {"form" : form})
