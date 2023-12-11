from django.urls import path
from . import views

### Localhost:8000/ ---- blog-home

### Localhost:8000/about ---- blog-about
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]