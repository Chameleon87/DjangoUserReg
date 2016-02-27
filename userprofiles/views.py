from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from forms import UserProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
class user_profile(request):
    form = UserProfileForm()
    if form.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/loggedin.html')
        else:
            form = UserProfileForm()
            return render(request, 'user_profile.html', { "form" : form })
    else:
        return render(request, 'user_profile.html', { "form" : form })
