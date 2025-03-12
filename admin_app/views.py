from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required


def login_required_decorator(func):
    return login_required(login_url="login_page")


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, password=password, username=username)
        if user is None:
            login(request, user)
            return redirect("home_page")

    return render(request, "login.html")