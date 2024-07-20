from django.shortcuts import render
from django.http import HttpResponse
from .models import prjvariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_newprjct(request):
    prjs = prjvariety.objects.all()
    return render(request, 'newprjct/all_newprjct.html', {'prjs': prjs})


def prj_detail(request, prj_id):
    prj = get_object_or_404(prjvariety, pk=prj_id)
    return render(request, 'newprjct/prj_detail.html', {'prj': prj})