from django.urls import path
from . import views

app_name = 'mentorapp'

urlpatterns = [
    path('', views.mentorhomepage, name='mentorhomepage'),
    path('addstudent/', views.add_student, name='addstudent'),
    path('studentlist/', views.student_list, name='studentlist'),
]