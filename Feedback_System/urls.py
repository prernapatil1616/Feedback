"""
URL configuration for Feedback_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views, HOD, STUDENT, FACULTY

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('base/', views.BASE, name='base'),
                  # login path
                  path('', views.LOGIN, name='login'),
                  path('doLogin', views.doLogin, name='doLogin'),
                  path('doLogout', views.doLogout, name='logout'),
                  #     this is hod panel url
                  path('HOD/Home', HOD.HOME, name='home'),
                  path('HOD/Student/Add', HOD.ADD_STUDENT, name='add_student'),
                  path('HOD/Student/View', HOD.VIEW_STUDENT, name='view_student'),
                  path('HOD/Student/Edit/<str:id>', HOD.EDIT_STUDENT, name='edit_student'),
                  path('HOD/Student/Update', HOD.UPDATE_STUDENT, name='update_student'),
                  path('HOD/Student/Delete/<str:admin>', HOD.DELETE_STUDENT, name='delete_student'),

                  # faculty panel
                  path('HOD/Faculty/Add', HOD.ADD_FACULTY, name='add_faculty'),
                  path('HOD/Faculty/View', HOD.VIEW_FACULTY, name='view_faculty'),
                  path('HOD/Faculty/Edit', HOD.EDIT_FACULTY, name='edit_faculty'),
                  path('HOD/Faculty/Edit/<str:id>', HOD.EDIT_FACULTY, name='edit_faculty'),
                  path('HOD/Student/Update', HOD.UPDATE_FACULTY, name='update_faculty'),
                  path('HOD/Student/Delete/<str:admin>', HOD.DELETE_FACULTY, name='delete_faculty'),

                  # student panel
                  path('HOD/Course/Add', HOD.ADD_COURSE, name='add_course'),
                  path('HOD/Course/View', HOD.VIEW_COURSE, name='view_course'),
                  path('HOD/Course/Edit/<str:id>', HOD.EDIT_COURSE, name='edit_course'),
                  path('HOD/Course/Update', HOD.UPDATE_COURSE, name='update_course'),
                  path('HOD/Course/Delete/<str:id>', HOD.DELETE_COURSE, name='delete_course'),

                  # profile update
                  path('profile', views.PROFILE, name='profile'),
                  path('profile/update', views.PROFILE_UPDATE, name='profile_update'),

                  # Faculty urls
                  path('Faculty/Home', FACULTY.HOME, name='faculty_home'),
                  # studdent panel
                  path('Student/Home', STUDENT.HOME, name='student_home'),
                  path('Student/feedback', STUDENT.STUDENT_FEEDBACK, name='student_feedback'),
                  path('Student/feedback/save', STUDENT.STUDENT_FEEDBACK_SAVE, name='student_feedback_save'),

                  #        feedback
                  # path('HOD/Feedback/Add', HOD.ADD_FEEDBACK, name='add_feedback'),
                  # path('HOD/Feedback/View', HOD.VIEW_FEEDBACK, name='view_feedback'),
                  # path('HOD/Feedback/Edit/<str:id>', HOD.EDIT_FEEDBACK, name='edit_feedback'),
                  # path('HOD/Feedback/Update', HOD.UPDATE_FEEDBACK, name='update_feedback'),
                  # path('HOD/Feedback/Delete/<str:id>', HOD.DELETE_FEEDBACK, name='delete_feedback'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
