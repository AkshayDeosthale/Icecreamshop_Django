from django.shortcuts import render, HttpResponse

# Create your views here.


def sample_function(request):
    return HttpResponse("This is homepage")
