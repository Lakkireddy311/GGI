from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



from django.core.mail import send_mail

# Add this import at the top, assuming you want to use the default email settings from settings.py
from django.conf import settings

@login_required(login_url='login')
def HomePage(request):
    
    return render(request, 'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')


def chat_view(request):
    return render(request, 'Chat.html')
def View_view(request):
    return render(request,'View.html')
def About_view(request):
    return render(request,'About.html')
def Contact_view(request):
    return render(request,'Contact.html')
def Privacy_view(request):
    return render(request,'Privacy.html')
def Terms_view(request):
    return render(request,'Terms.html')
def Settings_view(request):
    return render(request,'Settings.html')
def help_view(request):
    return render(request,'help.html')
def Careers_view(request):
    return render(request,'Careers.html')
def services_view(request):
    return render(request,'services.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


