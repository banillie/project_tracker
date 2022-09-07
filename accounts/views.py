from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _

from .forms import SignUpForm


@login_required
def change_password_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # don't logout user
            messages.success(request, _('Your password has been successfully updated!'))  # not doing anything?
            return redirect("home")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, "accounts/change_password.html", context)


def register_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')
    context = {"form": form}
    return render(request, "accounts/register.html", context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html", {})

