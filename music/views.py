from django.shortcuts import render, redirect
from .models import Audio
# Create your views here.

def home_page(request):
    audios = Audio.objects.all()[:5]
    return render(request,"music/home.html",{"audios":audios})

def detail_page(request,slug):
    audio = Audio.objects.filter(slug = slug).first()
    
    if audio:
        
        return render(request, "music/detail.html", {"audio":audio})
    
    else:
        return redirect("music:404")
    

def page_404(request):
    return render(request,"music/404.html",{})
    
