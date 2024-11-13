from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def corehomepage(request):
    return render(request, 'coreapp/corehomepage.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Mentor
from django.db import IntegrityError

def add_mentor(request):
    if request.method == 'POST':
        register_number = request.POST['Register_Number']
        name = request.POST['Name']
        domain = request.POST['Domain']
        try:
            user = User.objects.get(username=register_number)
            mentor = Mentor(register_number=register_number, name=name, domain=domain, user=user)
            mentor.save()
            return redirect('coreapp:mentorList')
        except User.DoesNotExist:
            return render(request, 'coreapp/addmentor.html', {'error': 'No user found with this Register Number'})
        except IntegrityError:
            return render(request, 'coreapp/addmentor.html', {'error': 'Mentor with this Register Number already exists'})
    return render(request, 'coreapp/addmentor.html')

def mentor_list(request):
    mentors = Mentor.objects.all()
    return render(request, 'coreapp/mentor_list.html', {'mentors': mentors})