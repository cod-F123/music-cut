from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import random

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
    
    def __str__(self):
        return self.name

class Singer(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="uplude/img/singer/",default="static/images/cello.jpg")
    description = models.TextField(blank=True,null=True)
    
    class Meta:
        verbose_name_plural = "Singers"
        verbose_name = "Singer"
    
    def __str__(self):
        return self.name

class Audio(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    audio = models.FileField(upload_to="upload/audio/")
    image = models.ImageField(upload_to="upload/img/audio/",default="static/images/cello-img.jpg")
    description = models.TextField(blank=True,null=True)
    
    slug = models.SlugField(unique=True,blank=True,null=True)
    
    date_add = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Audios"
        verbose_name = "Audio"
        ordering = ["-date_add"]
    
    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        
        # crate slug
        if not self.slug:
            random_num = random.randint(1000,10000)
            self.slug = slugify(self.name) + "-" + str(self.singer) + "-" + str(random_num)
            self.save()



class Comment(models.Model):
    audio = models.ForeignKey(Audio,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    date_create = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username