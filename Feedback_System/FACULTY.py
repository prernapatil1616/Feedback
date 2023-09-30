from django.shortcuts import render, redirect


def HOME(request):
    return render(request, 'FACULTY/faculty_home.html')
