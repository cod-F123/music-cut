from django.contrib import admin 
from .models import Category , Singer , Audio , Comment

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ["name","singer","category"]
    readonly_fields = ["date_add","slug"]
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user","audio"]
    readonly_fields = ["date_create"]