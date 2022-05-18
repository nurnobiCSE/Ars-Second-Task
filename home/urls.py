from django.urls import path
from .import views
urlpatterns = [
    path('home/',views.index,name='index'),
    path('register-user/',views.User_Register,name='register'),
    path('',views.loginPage,name='login'),
    path('logout',views.logoutUser, name='logout')
]

