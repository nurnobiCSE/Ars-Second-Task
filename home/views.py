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
    post = create_post.objects.all()
    stori = Stories.objects.all()
    profiles = Profile.objects.last()

    if request.method == "POST":
        form = ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            # obj = form.instance
            # return render(request,"index.html",{"obj":obj})
        # upload_data = request.FILES['upload']
        # fss = FileSystemStorage()
        # fss.save(upload_data.name, upload_data)

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

    return render(request,'login.html')

