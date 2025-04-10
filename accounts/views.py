from django.shortcuts import render , redirect
from django.urls import reverse
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request,user)
                return redirect("music:home")
            
            else:
                return redirect("login")
        else:
            return render(request,"accounts/login.html",{})
        
    else:
        return redirect("home") 


@login_required
def logout_user(request):
    logout(request)
    return redirect("music:home")

def register(request):
    if not request.user.is_authenticated:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            print(form)
            if form.is_valid():
                form.save()
                print(1)
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password2"]
                
                user = authenticate(username= username,password=password)
                
                if user is not None:
                    login(request,user)
                    return redirect("music:home")
                else:
                    return redirect("register")
            else:
                return redirect("register")
        else:
            return render(request,"accounts/signup.html",{"form":form})
    else:
        return redirect("music:home")