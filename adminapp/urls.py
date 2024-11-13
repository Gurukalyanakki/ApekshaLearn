from django.urls import path
from . import views

app_name = 'adminapp'

urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),
    path('projecthomepage2/', views.projecthomepage2, name='projecthomepage2'),
    path('login/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('login-logic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('register-logic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('cou', views.courosel, name='courosel'),
     path('contactuss', views.contact, name='contactus'),
    
]
