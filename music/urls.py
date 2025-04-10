from django.urls import path 
from . import views 

app_name = "music"

urlpatterns = [
    path("",views.home_page,name="home"),
    path("music/<str:slug>/",views.detail_page,name="detail"),
    path("ERROR404/",views.page_404,name="404"),
    path("music/<str:slug>/comment/new/",views.crete_comment,name="create_comment"),
]
