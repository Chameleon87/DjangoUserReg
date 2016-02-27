from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userprofiles.forms import UserProfileForm


# Create your views here.
@login_required
def user_profile(request):
    form = UserProfileForm()
    if form.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/user_profile.html')
        else:
            form = UserProfileForm()
            return render(request, 'user_profile.html', {"form" : form})
    else:
        return render(request, 'user_profile.html', {"form" : form})
