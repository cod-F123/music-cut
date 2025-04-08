from django.contrib import admin 
from .models import Category , Singer , Audio

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