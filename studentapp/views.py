from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def studenthomepage(request):
    return render(request, 'studentapp/studenthomepage.html')

def variablesandconstantsc(request):
    return render(request, 'studentapp/variablesandconstantsc.html')
def datatypes(request):
    return render(request, 'studentapp/cdatatypes.html')
def inoutc(request):
    return render(request, 'studentapp/inputoutputc.html')
def operators(request):
    return render(request, 'studentapp/operatorsc.html')
def  logicoperators(request):
    return render(request, 'studentapp/logicoperatorsc.html')
def  conditionalst(request):
    return render(request, 'studentapp/conditionalstc.html')
def  loop(request):
    return render(request, 'studentapp/loopstc.html')
def  func(request):
    return render(request, 'studentapp/functions.html')
def  array(request):
    return render(request, 'studentapp/carrays.html')
def  strings(request):
    return render(request, 'studentapp/cstrings.html')
def  pointer(request):
    return render(request, 'studentapp/cpointers.html')
def  uddatatypes(request):
    return render(request, 'studentapp/userdefineddatatypes.html')
def  Storageclass(request):
    return render(request, 'studentapp/Storageclass.html')
def  fileh(request):
    return render(request, 'studentapp/Filehandling.html')
















