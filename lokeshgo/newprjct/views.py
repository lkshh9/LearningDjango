from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def all_newprjct(request):
    return render(request, 'newprjct/all_newprjct.html')
