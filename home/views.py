from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.

def index(request):
    return render(request, 'home.html')

def signup(request):
    if request.method=='POST':
        username = request.POST['user']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pwd']   
        
        a = User.objects.create_user(username=username, first_name = name, email=email, password = password)
        a.save()
        auth.login(request,
                  a)
        return redirect('/')
        
    else: 
        return render(request, 'signup.html')
    
    
def login(request):
    if request.method=='POST':
        username1 = request.POST['user1']
        password1 = request.POST['pwd1']    
        x = auth.authenticate(username = username1, password = password1)
        if x is not None:
            auth.login(request, x)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')
