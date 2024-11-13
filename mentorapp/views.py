from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def mentorhomepage(request):
    return render(request, 'mentorapp/mentorhomepage.html')


from .models import Student
def add_student(request):
    if request.method == 'POST':
        register_number = request.POST['Register_Number']
        name = request.POST['Name']
        try:
            user = User.objects.get(username=register_number)
            student = Student(register_number=register_number, name=name, user=user)
            student.save()
            return redirect('mentorapp:studentlist')
        except User.DoesNotExist:
            return render(request, 'mentorapp/addstudent.html', {'error': 'No user found with this Register Number'})
        except IntegrityError:
            return render(request, 'mentorapp/addstudent.html', {'error': 'Mentor with this Register Number already exists'})
    return render(request, 'mentorapp/addstudent.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'mentorapp/student_list.html', {'students': students})