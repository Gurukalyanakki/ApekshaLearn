from django.urls import path
from . import views

app_name = 'coreapp'

urlpatterns = [
path('', views.corehomepage, name='corehomepage'),
path('addMentor',views.add_mentor,name="addMentor"),
path('mentorList/',views.mentor_list,name='mentorList'),


]