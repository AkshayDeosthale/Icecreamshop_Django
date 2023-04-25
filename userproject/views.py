from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout


# Create your views here.


def serveLoginPage(request):
    if request.user.is_anonymous:
        return render(request, "login.html")
    else:
        return redirect("/")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            return redirect("/")
        else:
            return render(request, "login.html")


def logoutuser(request):
    logout(request)
    return render(request, "login.html")


def signupuser(request):
    if request.method == "POST":
        # something
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")

        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
        )
        user.save()
        return render(request, "login.html")
    else:
        return render(request, "signup.html")
