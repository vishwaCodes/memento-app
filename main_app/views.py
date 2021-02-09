from django.shortcuts import render
from django.http import HttpResponse
from .models import Photobook, Photo


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    photobooks = Photobook.objects.all()
    photos = Photo.objects.all()
    
    context = {'photobooks': photobooks, 'photos': photos}
    return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})

def addPhoto(request):
    return render(request, 'photos/add.html')