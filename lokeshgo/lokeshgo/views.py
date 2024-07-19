from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello haters, you are at my mercy home page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello haters, you are at my mercy About page")

def contact(request):
    return HttpResponse("Hello haters, you are at my mercy Slaughter page")