from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.


async def homepage_function(request):
    context = {"variable": "Akshay Deosthale"}
    return render(request, "index.html", context)


async def aboutpage_function(request):
    return render(request, "about.html")


async def servicepage_function(request):
    return render(request, "service.html")


def constactpage_function(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        description = request.POST.get("description")
        contacts = Contact(
            fullname=fullname,
            email=email,
            phone=phone,
            description=description,
            date=datetime.today(),
        )
        contacts.save()
        messages.success(request, "Thank you for your query.")

    return render(request, "contact.html")
