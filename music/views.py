from django.shortcuts import render, redirect
from django.urls import reverse , reverse_lazy
from .models import Audio
from .forms import CommentForm

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
    

def crete_comment(request,slug):
    if request.user.is_authenticated:
        audio = Audio.objects.filter(slug = slug).first()
        if audio:
            if request.method == "POST":
                form = CommentForm(request.POST)
                if form.is_valid():
                    user = request.user 
                    form.instance.user = user 
                    form.instance.audio = audio
                    form.save()
                    return redirect(reverse("music:detail",args=[slug]))
            else:
                form = CommentForm()
                return render(request,"music/create_comment.html",{"form":form})
        else:
            redirect("music:404")
    else:
        return redirect("login")
    

def page_404(request):
    return render(request,"music/404.html",{})
    
