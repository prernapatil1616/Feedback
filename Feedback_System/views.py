from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser


def BASE(request):
    return render(request, 'base.html')


def LOGIN(request):
    return render(request, 'Login.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackend.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'), )

        if user !=  None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('home')
            elif user_type == '2':
                return redirect('faculty_home')
            elif user_type == '3':
                return redirect('student_home')
            else:
                messages.error(request, 'Email or Password are invalid')

                return redirect('login')
        else:
            messages.error(request, 'Email or Password are invalid')
            return redirect('login')



def doLogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        "user": user,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name

            if profile_pic:
                customuser.profile_pic = profile_pic

            if password:
                customuser.set_password(password)

            customuser.save()
            messages.success(request, 'Your Profile Updated Successfully!')
            return redirect('profile')  # Redirect to the appropriate view or URL

        except CustomUser.DoesNotExist:
            messages.error(request, 'Failed to update profile')

        return render(request, 'profile.html')
