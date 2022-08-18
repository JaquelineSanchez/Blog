from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("Bienvenid@ a mi blog") #Texto plano
    return render(request,"blog/home.html")