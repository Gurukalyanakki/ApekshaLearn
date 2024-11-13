from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def projecthomepage(request):
    return render(request, 'adminapp/projecthomepage.html')

def contact(request):
    return render(request, 'adminapp/contactus.html')

def projecthomepage2(request):
    return render(request, 'adminapp/projecthomepage2.html')

def UserLoginPageCall(request):
    return render(request, 'adminapp/login.html')

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                messages.success(request, 'Login successful as student!')
                return redirect('adminapp:courosel')
            elif len(username) == 5:
                return redirect('mentorapp:mentorhomepage')
            elif len(username) == 7:
                return redirect('coreapp:corehomepage')
            else:
                messages.error(request, 'Username length does not match criteria.')
                return render(request, 'adminapp/login.html')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/login.html')
    return render(request, 'adminapp/login.html')

def logout(request):
    auth.logout(request)
    return redirect('adminapp:projecthomepage2')

def UserRegisterPageCall(request):
    return render(request, 'adminapp/register.html')

def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/register.html')
    return render(request, 'adminapp/register.html')
  
  

def courosel(request):
    return render(request, 'adminapp/courosel.html')