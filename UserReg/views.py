from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse
from forms import RegistrationForm




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

def loggedin(request):
    return render_to_response('accounts/loggedin.html',
                    {'full_name': request.user.username})

def invalid_login(request):
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
            return render(request, 'accounts/register_success.html')
        else:
            return render(request, 'accounts/register.html',
                    { "form" : form })
    else:
        return render(request, 'accounts/register.html',
                { "form" : form })


def register_success(request):
    return render_to_response('register_success.html')

@login_required
def user_profile(request):
    form = UserProfileForm()
    """ User Profile Page """
    u = User.objects.get(pk=request.user.pk)
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/user_profile.html')
        else:
            return render(request, 'accounts/user_profile.html',
                    { "form" : form })
    else:
        return render_to_response('accounts/user_profile.html', {
        "user" : request.user,
        "form" : form,
        })
