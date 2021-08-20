from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return render(request, 'base/home.html')

def test(request):
    return render(request, 'base/test.html')

def test1(request):
    return render(request, 'base/test1.html')

def info(request):
    return render(request, 'base/info.html')

