from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return render(request, 'base/home.html')

def info(request):
    return render(request, 'base/info.html')

def draft(request):
    return render(request, 'base/draft.html')
