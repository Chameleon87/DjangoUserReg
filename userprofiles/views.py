from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userprofiles.forms import UserProfileForm


# Create your views here.
@login_required
def user_profile(request):
        return render(request, 'accounts/user_profile.html')

@login_required
def edit_user_profile(request):
    if request.method == "POST":
        print "a"
        form = UserProfileForm(data=request.POST, instance=request.user.profile)
        if form.is_valid():
            print "b"
            form.save()
            return render(request, 'accounts/user_profile.html')
        else:
            print "c"
            return render(request, 'accounts/edit_profile.html', {"form" : form })
    else:
        print "e"
        form = UserProfileForm()
        if form.is_valid():
            form.save()
            return render(request, 'accounts/user_profile.html')
        else:
            print "d"
            return render(request, 'accounts/edit_profile.html', {"form" : form })
