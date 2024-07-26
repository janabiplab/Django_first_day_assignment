from django.urls import path
from .import views

urlpatterns = [
    path('list/',views.home,name="home"),
    path('list/<int:idd>/',views.blog_details,name="blog_details")
]