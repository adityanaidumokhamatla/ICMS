from django.shortcuts import render

def indexrender(request):
    return render(request, "index.html")
def homerender(request):
    return render(request,"index2.html")
def contactusrender(request):
    return render(request,"contactus.html")

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')
def Register(request):
    return render(request,'sign.html')
def signup1(request):
    if request.method == "POST":
        username = request.POST['username']
        email= request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists()or User.objects.filter(email=email):
                messages.info(request, 'OOPS! Username Already Exists')
                return render(request, 'sign.html')
            else:
                user = User.objects.create_user(username=username, password=pass1,email=email)
                user.save()

                messages.success(request, "Account Created")
                return render(request, 'login.html')
        else:
            messages.error(request, 'Password do not match')
            return render(request, 'sign.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index2')
        else:
            messages.error(request, 'Invalid username or password.')

            return render(request, 'login.html')

    return render(request, 'login.html')

def index2(request):
    return render(request, "index2.html")
def logout(request):
    auth.logout(request)
    return redirect('index')

