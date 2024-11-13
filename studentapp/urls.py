from django.urls import path
from . import views

app_name = 'studentapp'


urlpatterns = [
path('', views.studenthomepage, name='studenthomepage'),
path('varconc/', views.variablesandconstantsc, name='variablesandconstantsc'),
path('type/', views.datatypes, name='cdatatypes'),
path('inout/', views.inoutc, name='inputoutputc'),
path('operator/', views.operators, name='operatorsc'),
path('logicoperator/', views.logicoperators, name='logicoperatorsc'),
path('conditional/', views.conditionalst, name='conditionalstc'),
path('loop/', views.loop, name='loopstc'),
path('func/', views.func, name='functions'),
path('arr/', views.array, name='carrays'),
path('str/', views.strings, name='cstrings'),
path('poi/', views.pointer, name='cpointers'),
path('uddt/', views.uddatatypes, name='userdefineddatatypes'),
path('storage/', views.Storageclass, name='Storageclass'),
path('file/', views.fileh, name='Filehandling'),





]