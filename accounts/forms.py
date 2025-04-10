from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

# Create RegisterForm
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="",
        max_length=200,
        widget= forms.TextInput(attrs={"placeholder":"username"}),
        required=True
    )
    
    email = forms.EmailField(
        label="",
        max_length=300,
        widget=forms.EmailInput(attrs={"placeholder":"email"}),
        required=False
    )
    
    password1 = forms.CharField(
        label="",
        max_length=20,
        min_length=8,
        widget=forms.PasswordInput(attrs={"placeholder":"password","name":"password"}),
        required=True
    )
    
    password2 = forms.CharField(
        label="",
        max_length=20,
        min_length=8,
        widget=forms.PasswordInput(attrs={"placeholder":"password","name":"password"}),
        required=True
    )
    
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]