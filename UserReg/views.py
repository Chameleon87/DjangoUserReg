from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf

def index(request):
    return render_to_response('index.html', RequestContext(request))

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('accounts/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('accounts/loggedin')
    else:
        return HttpResponseRedirect('accounts/invalid')

def loggedin(request):
    return render_to_response('accounts/loggedin.html',
            {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('accounts/invalid_login.html')

def logout(request):
    auth.logout(request)
    render_to_response('accounts/logout.html')
