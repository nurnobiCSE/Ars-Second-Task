from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register-user/',views.User_Register,name='register'),
    path('login-user/',views.loginPage,name='login')
]

