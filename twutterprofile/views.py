from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from twutterprofile.forms import SignupForm, SigninForm
from twuut.forms import TwuutForm

def return_to_top():
    top_url = reverse("profile:frontpage")
    return redirect(top_url)

@login_required
def profile(request, username):
    # User profile view. allows you to view other users' information.
    user = User.objects.get(username=username)

    if request.method == 'POST':
        form = TwuutForm(data=request.POST)

        if form.is_valid():
            twuut = form.save(commit=False)
            twuut.user = request.user
            twuut.save()
        redirecturl = request.POST.get('redirect', reverse("profile:frontpage"))
        return redirect(redirecturl)
    else:
        form = TwuutForm()
    return render(request, 'profile.html', {'form': form, 'user': user})


def frontpage(request):
    if request.user.is_authenticated:
        return redirect(reverse("profile:profile", args=[request.user.username]))
    if request.method == 'POST':
        if 'signupform' in request.POST:
            signupform = SignupForm(data=request.POST)
            signinform = SigninForm()

            if signupform.is_valid():
                username = signupform.cleaned_data['username']
                password = signupform.cleaned_data['password1']
                signupform.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                return return_to_top()
        else:
            signinform = SigninForm(data=request.POST)
            signupform = SignupForm()

            if signinform.is_valid():
                login(request, signinform.get_user())
                return return_to_top()
    else:
        signupform = SignupForm()
        signinform = SigninForm()

    return render(request, 'frontpage.html', {'signupform': signupform, 'signinform': signinform}) # noqa


def signout(request):
    logout(request)
    return return_to_top()


def follows(request, username):
    user = User.objects.get(username=username)
    twutterprofiles = user.twutterprofile.follows.select_related('user').all()
    return render(request, 'users.html', {'title': 'Follows', 'twutterprofiles': twutterprofiles})  # noqa


def followers(request, username):
    user = User.objects.get(username=username)
    twutterprofiles = user.twutterprofile.followed_by.select_related('user').all() # noqa
    return render(request, 'users.html', {'title': 'Followers', 'twutterprofiles': twutterprofiles})  # noqa


@login_required
def follow(request, username):
    user = User.objects.get(username=username)
    request.user.twutterprofile.follows.add(user.twutterprofile)
    return HttpResponseRedirect('/' + user.username + '/')


@login_required
def stopfollow(request, username):
    user = User.objects.get(username=username)
    request.user.twutterprofile.follows.delete(user.twutterprofile)
    return HttpResponseRedirect('/' + user.username + '/')
