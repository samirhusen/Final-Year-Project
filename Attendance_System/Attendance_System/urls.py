"""Attendance_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path
from Attendance_System import settings
from Attendance_System_App import views, AdminViews, TeacherViews, StudentViews, StudentServiceStaffViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ShowLoginPage,name="show_login"),
    path('doLogin',views.doLogin,name="do_login"),
    path('get_user_details',views.GetUserDetails),
    path('logout_user',views.logout_user,name="logout"),
    path('admin_home',AdminViews.admin_home,name="admin_home"),
    path('add_teacher',AdminViews.add_teacher,name="add_teacher"),
    path('add_teacher_save',AdminViews.add_teacher_save,name="add_teacher_save"),
    path('add_student_service_staff',AdminViews.add_student_service_staff,name="add_student_service_staff"),
    path('add_student_service_staff_save',AdminViews.add_student_service_staff_save,name="add_student_service_staff_save"),
    path('add_course',AdminViews.add_course,name="add_course"),
    path('add_course_save',AdminViews.add_course_save,name="add_course_save"),
    path('add_student',AdminViews.add_student,name="add_student"),
    path('add_student_save',AdminViews.add_student_save,name="add_student_save"),
    path('add_subject',AdminViews.add_subject,name="add_subject"),
    path('add_subject_save',AdminViews.add_subject_save,name="add_subject_save"),
    path('manage_teacher',AdminViews.manage_teacher,name="manage_teacher"),
    path('manage_student',AdminViews.manage_student,name="manage_student"),
    path('manage_student_service_staff',AdminViews.manage_student_service_staff,name="manage_student_service_staff"),
    path('manage_course',AdminViews.manage_course,name="manage_course"),
    path('manage_subject',AdminViews.manage_subject,name="manage_subject"),
    path('edit_teacher/<str:teacher_id>',AdminViews.edit_teacher,name="edit_teacher"),
    path('edit_teacher_save',AdminViews.edit_teacher_save, name="edit_teacher_save"),
    path('edit_student_service_staff/<str:studentservicestaff_id>',AdminViews.edit_student_service_staff,name="edit_student_service_staff"),
    path('edit_student_service_staff_save',AdminViews.edit_student_service_staff_save, name="edit_student_service_staff_save"),
    path('edit_student/<str:student_id>',AdminViews.edit_student, name="edit_student"),
    path('edit_student_save',AdminViews.edit_student_save, name="edit_student_save"),
    path('edit_subject/<str:subject_id>',AdminViews.edit_subject, name="edit_subject"),
    path('edit_subject_save',AdminViews.edit_subject_save, name="edit_subject_save"),
    path('edit_course/<str:course_id>',AdminViews.edit_course, name="edit_course"),
    path('edit_course_save',AdminViews.edit_course_save, name="edit_course_save"),

# Teacher URL Path
    path('teacher_home',TeacherViews.teacher_home,name="teacher_home"),

# Student URL Path
    path('student_home',StudentViews.student_home,name="student_home"),

#Studnet Service Staff URL Path
    path('studentservicestaff_home',StudentServiceStaffViews.studentservicestaff_home,name="studentservicestaff_home")



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

