from django.shortcuts import render
from django.template import loader
from photos.models import Photo

def index(request):
    context = {
        "photos" : Photo.objects.all()
        }
    return render(request, "photos/index.html", context)