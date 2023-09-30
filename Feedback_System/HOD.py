from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Course, CustomUser, Student, Faculty
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    faculty_count = Faculty.objects.all().count()
    course_count = Course.objects.all().count()

    student_gender_male = Student.objects.filter(gender='Male').count()
    student_gender_female = Student.objects.filter(gender='Female').count()

    context = {
        'student_count': student_count,
        'faculty_count': faculty_count,
        'course_count': course_count,
        'student_gender_male': student_gender_male,
        'student_gender_female': student_gender_female,
    }

    return render(request, 'HOD/home.html', context)


@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already Exist')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'username is already Exist')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                profile_pic=profile_pic,
                user_type=3,
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)

            student = Student(
                admin=user,
                course_id=course,
                gender=gender,
            )
            student.save()
            messages.success(request, user.first_name + " " + user.last_name + ' Successfully Aadded')
            return redirect('add_student')

    context = {
        'course': course,
    }
    return render(request, 'HOD/add_student.html', context)


def VIEW_STUDENT(request):
    student = Student.objects.all()

    context = {
        'student': student,
    }
    return render(request, 'HOD/view_student.html', context)


def EDIT_STUDENT(request, id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    context = {
        'student': student,
        'course': course,
    }

    return render(request, 'HOD/edit_student.html', context)


def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')

        user = CustomUser.objects.get(id=student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin=student_id)
        student.gender = gender

        course = Course.objects.get(id=course_id)
        student.course_id = course

        student.save()
        messages.success(request, 'Records are successfully updated!')
        return redirect('view_student')

    return render(request, 'HOD/edit_student.html')


def DELETE_STUDENT(request, admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request, 'Records are successfully Deleted! ')
    return redirect('view_student')


def ADD_COURSE(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')

        course = Course(
            name=course_name,
        )
        course.save()
        messages.success(request, 'Course are successfully added!')
        return redirect('add_course')

    return render(request, 'HOD/add_course.html')


def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course': course,
    }
    return render(request, 'HOD/view_course.html', context)


def EDIT_COURSE(request, id):
    course = Course.objects.get(id=id)

    context = {
        'course': course,
    }
    return render(request, 'HOD/edit_course.html', context)


def UPDATE_COURSE(request):
    if request.method == "POST":
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id=course_id)
        course.name = name
        course.save()
        messages.success(request, 'Course are successfully updated!')
        return redirect('view_course')
    return render(request, 'HOD/edit_course.html')


def DELETE_COURSE(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Course are successfully deleted')
    return redirect('view_course')


def ADD_FACULTY(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already Exist')
            return redirect('add_faculty')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'username is already Exist')
            return redirect('add_faculty')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                profile_pic=profile_pic,
                user_type=2,
            )
            user.set_password(password)
            user.save()

            faculty = Faculty(
                admin=user,
                gender=gender,
            )
            faculty.save()
            messages.success(request, 'Added Successfully ')
            return redirect('add_faculty')

    return render(request, 'HOD/add_faculty.html')


def VIEW_FACULTY(request):
    faculty = Faculty.objects.all()

    context = {
        'faculty': faculty,
    }

    return render(request, 'HOD/view_faculty.html', context)


def EDIT_FACULTY(request, id):
    faculty = Faculty.objects.filter(id=id)

    context = {
        'faculty': faculty,
    }

    return render(request, 'HOD/edit_faculty.html', context)


def UPDATE_FACULTY(request):
    if request.method == "POST":
        faculty_id = request.POST.get('faculty_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id=faculty_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        faculty = Faculty.objects.get(admin=faculty_id)
        faculty.gender = gender

        faculty.save()
        messages.success(request, 'Updated successfully!')
        return redirect('view_faculty')

    return render(request, 'HOD/edit_faculty.html')


def DELETE_FACULTY(request, admin):
    faculty = CustomUser.objects.get(id=admin)
    faculty.delete()
    messages.success(request, 'Deleted successfully! ')
    return redirect('view_faculty')

#
# def ADD_FEEDBACK(request):
#     if request.method == 'POST':
#         options_name = request.POST.get('options_name')
#
#         option = Feedback(
#             name=options_name,
#         )
#         option.save()
#         messages.success(request, 'Added Successfully')
#         return redirect('add_feedback')
#     return render(request, 'HOD/add_feedback.html')
#
#
# def VIEW_FEEDBACK(request):
#     option = Feedback.objects.all()
#
#     context = {
#         'option': option,
#     }
#
#     return render(request, 'HOD/view_feedback.html', context)
#
#
# def EDIT_FEEDBACK(request, id):
#     option = Feedback.objects.get(id=id)
#
#     context = {
#         'option': option,
#     }
#     return render(request, 'HOD/edit_feedback.html', context)
#
#
# def UPDATE_FEEDBACK(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         option_id = request.POST.get('option_id')
#
#         option = Feedback.objects.get(id=option_id)
#         option.name = name
#         option.save()
#         messages.success(request, 'Updated successfully!')
#         return redirect('view_feedback')
#     return render(request, 'HOD/edit_feedback.html')
#
#
# def DELETE_FEEDBACK(request,id):
#     option = Feedback.objects.get(id=id)
#     option.delete()
#     messages.success(request, 'Deleted Successfully ')
#     return redirect('view_feedback')
