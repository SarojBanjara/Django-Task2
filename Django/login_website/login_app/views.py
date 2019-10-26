from django.shortcuts import render

# Create your views here.

def form(request):

    return render(request,'login.html')

def next_page(request):
    username = request.POST["username"]
    email = request.POST["email"]
    return render(request,'congo.html',{'username':username, 'email':email})