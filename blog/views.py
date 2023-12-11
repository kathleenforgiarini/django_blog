from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

# posts = [
#     {
#         'author' : 'Marry',
#         'title' : 'Post 1',
#         'content' : 'The First Post Blog',
#         'date_posted' : '12 Jul 2023'
#     },
#     {
#         'author' : 'James',
#         'title' : 'Post 2',
#         'content' : 'The Second Post Blog',
#         'date_posted' : '22 Jul 2023'
#     }
# ]

def home(request):
    #return HttpResponse("<h1> Home Page </h1>")
    return render(request, 'blog/home.html', {'posts' : Post.objects.all(), 'title' : 'Home Page'})

def about(request):
    #return HttpResponse("<h1> About Page </h1>")
    return render(request, 'blog/about.html', {'title' : 'About'})
