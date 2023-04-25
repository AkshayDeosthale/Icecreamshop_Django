from django.contrib import admin
from django.urls import path, include
from userproject import views

urlpatterns = [
    path("", views.serveLoginPage, name="userproject"),
    path("signin", views.login, name="signin"),
    path("signout", views.logoutuser, name="signout"),
    path("signup", views.signupuser, name="signup"),
]
