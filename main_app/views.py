from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def photobooks(request):
    return render (request, 'photobooks/index.html', { 'photobooks': photobooks })