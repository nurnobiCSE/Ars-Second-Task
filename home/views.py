from django.shortcuts import render,HttpResponse,redirect
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