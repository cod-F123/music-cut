from django.shortcuts import render
from .models import Audio
# Create your views here.

def home_page(request):
    audios = Audio.objects.all()
    return render(request,"music/home.html",{"audios":audios})
