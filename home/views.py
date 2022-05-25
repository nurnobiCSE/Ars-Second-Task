from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
# import models here
from .models import *
from .form import ImageForm
# Create your views here.
def index(request):
    post = create_post.objects.all().order_by('-id')
    stori = Stories.objects.all().order_by('-id')
    profiles = Profile.objects.last()

    current_user = request.user


    if request.method == "POST":
        if request.POST.get('text'):
            form = create_post(
                text=request.POST['text'],
                upload=request.FILES['upload'],
                author_name=current_user.first_name,
                feelings=request.POST['feelings'],
                places=request.POST['places']
            )
            form.save()
            return redirect('index')
        if request.POST.get('stories_text'):
            form2 = Stories(
                img=request.FILES['stories_files'],
                title=request.POST['stories_text'],

            )
            form2.save()
            return redirect('index')


    context = {
        'post':post,
        'stori':stori,
        'profiles':profiles
    }
    return render(request,'index.html',context)

def User_Register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        user_info = Registerd_user(
            name = name,
            email = email,
            password = password1,
            rePass = password2
        )
        user_info.save()
    if request.method == "POST":
        username = request.POST['email']
        first_name = request.POST['name']
        password = request.POST['password1']
        rePass = request.POST['password2']

        if password == rePass:
            if User.objects.filter(username=username).exists():
                messages.warning(request,"this user already exist")
            else:
                user = User.objects.create_user(username=username,password=password,first_name=first_name)
                user.save()
                messages.success(request,"user registered!")
                return redirect('login')

    return render(request,'register.html')

def loginPage(request):
    if request.method =="POST":
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')

    return render(request,'login.html')

def logoutUser(request):
    auth.logout(request)
    return redirect('login')

