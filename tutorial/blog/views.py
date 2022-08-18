from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.

def home(request):
    #return HttpResponse("Bienvenid@ a mi blog") #Texto plano
    posts = Post.objects.all()
    return render(request,"blog/home.html",{'posts':posts})