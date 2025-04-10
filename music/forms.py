from django import forms 
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        max_length=300,
        label="",
        widget=forms.Textarea(attrs={"placeholder":"نظرخودرا بنویسید.."}),
        required=True
    )
    
    class Meta:
        model = Comment
        fields = ("content",)
    