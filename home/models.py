from django.db import models

# Create your models here.
class create_post(models.Model):
    text = models.CharField(max_length=1000,blank=True)
    upload = models.ImageField(blank=True,upload_to='postImg/')
    # description = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.text

class Stories(models.Model):
    img = models.ImageField(blank=True,upload_to='storisImg/')
    title = models.CharField(max_length=200,blank=True)

class Profile(models.Model):
    img = models.ImageField(upload_to='profileImg/',blank=True)
    name = models.CharField(max_length=30,blank=True)
    email = models.EmailField(max_length=100,blank=True)
    description = models.CharField(max_length=300,blank=True)

