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
from django.urls import path, include
from Attendance_System import settings
from Attendance_System_App import views, AdminViews, TeacherViews, StudentViews, StudentServiceStaffViews

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('', views.ShowLoginPage, name="show_login"),
                  path('doLogin', views.doLogin, name="do_login"),
                  path('get_user_details', views.GetUserDetails),
                  path('logout_user', views.logout_user, name="logout"),
                  path('admin_home', AdminViews.admin_home, name="admin_home"),
                  path('add_teacher', AdminViews.add_teacher, name="add_teacher"),
                  path('add_teacher_save', AdminViews.add_teacher_save, name="add_teacher_save"),
                  path('add_student_service_staff', AdminViews.add_student_service_staff,
                       name="add_student_service_staff"),
                  path('add_student_service_staff_save', AdminViews.add_student_service_staff_save,
                       name="add_student_service_staff_save"),
                  path('add_course', AdminViews.add_course, name="add_course"),
                  path('add_course_save', AdminViews.add_course_save, name="add_course_save"),
                  path('add_student', AdminViews.add_student, name="add_student"),
                  path('add_student_save', AdminViews.add_student_save, name="add_student_save"),
                  path('add_subject', AdminViews.add_subject, name="add_subject"),
                  path('add_subject_save', AdminViews.add_subject_save, name="add_subject_save"),
                  path('manage_teacher', AdminViews.manage_teacher, name="manage_teacher"),
                  path('manage_student', AdminViews.manage_student, name="manage_student"),
                  path('manage_student_service_staff', AdminViews.manage_student_service_staff,
                       name="manage_student_service_staff"),
                  path('manage_course', AdminViews.manage_course, name="manage_course"),
                  path('manage_subject', AdminViews.manage_subject, name="manage_subject"),
                  path('edit_teacher/<str:teacher_id>', AdminViews.edit_teacher, name="edit_teacher"),
                  path('edit_teacher_save', AdminViews.edit_teacher_save, name="edit_teacher_save"),
                  path('edit_student_service_staff/<str:studentservicestaff_id>', AdminViews.edit_student_service_staff,
                       name="edit_student_service_staff"),
                  path('edit_student_service_staff_save', AdminViews.edit_student_service_staff_save,
                       name="edit_student_service_staff_save"),
                  path('edit_student/<str:student_id>', AdminViews.edit_student, name="edit_student"),
                  path('edit_student_save', AdminViews.edit_student_save, name="edit_student_save"),
                  path('edit_subject/<str:subject_id>', AdminViews.edit_subject, name="edit_subject"),
                  path('edit_subject_save', AdminViews.edit_subject_save, name="edit_subject_save"),
                  path('edit_course/<str:course_id>', AdminViews.edit_course, name="edit_course"),
                  path('edit_course_save', AdminViews.edit_course_save, name="edit_course_save"),
                  path('manage_session', AdminViews.manage_session, name="manage_session"),
                  path('add_session_save', AdminViews.add_session_save, name="add_session_save"),

                  # path('check_email_exist', HodViews.check_email_exist, name="check_email_exist"),
                  # path('check_username_exist', HodViews.check_username_exist, name="check_username_exist"),
                  # path('student_feedback_message', HodViews.student_feedback_message, name="student_feedback_message"),
                  # path('student_feedback_message_replied', HodViews.student_feedback_message_replied,
                  #      name="student_feedback_message_replied"),
                  # path('staff_feedback_message', HodViews.staff_feedback_message, name="staff_feedback_message"),
                  # path('staff_feedback_message_replied', HodViews.staff_feedback_message_replied,
                  #      name="staff_feedback_message_replied"),
                  # path('student_leave_view', HodViews.student_leave_view, name="student_leave_view"),
                  # path('staff_leave_view', HodViews.staff_leave_view, name="staff_leave_view"),
                  # path('student_approve_leave/<str:leave_id>', HodViews.student_approve_leave,
                  #      name="student_approve_leave"),
                  # path('student_disapprove_leave/<str:leave_id>', HodViews.student_disapprove_leave,
                  #      name="student_disapprove_leave"),
                  # path('staff_disapprove_leave/<str:leave_id>', HodViews.staff_disapprove_leave,
                  #      name="staff_disapprove_leave"),
                  # path('staff_approve_leave/<str:leave_id>', HodViews.staff_approve_leave, name="staff_approve_leave"),
                  # path('admin_view_attendance', HodViews.admin_view_attendance, name="admin_view_attendance"),
                  # path('admin_get_attendance_dates', HodViews.admin_get_attendance_dates,
                  #      name="admin_get_attendance_dates"),
                  # path('admin_get_attendance_student', HodViews.admin_get_attendance_student,
                  #      name="admin_get_attendance_student"),
                  # path('admin_profile', HodViews.admin_profile, name="admin_profile"),
                  # path('admin_profile_save', HodViews.admin_profile_save, name="admin_profile_save"),
                  # path('admin_send_notification_staff', HodViews.admin_send_notification_staff,
                  #      name="admin_send_notification_staff"),
                  # path('admin_send_notification_student', HodViews.admin_send_notification_student,
                  #      name="admin_send_notification_student"),
                  # path('send_student_notification', HodViews.send_student_notification,
                  #      name="send_student_notification"),
                  # path('send_staff_notification', HodViews.send_staff_notification, name="send_staff_notification"),

                  # Teacher URL Path
                  path('teacher_home', TeacherViews.teacher_home, name="teacher_home"),
                  path('teacher_take_attendance', TeacherViews.teacher_take_attendance, name="teacher_take_attendance"),
                  path('teacher_update_attendance', TeacherViews.teacher_update_attendance,
                       name="teacher_update_attendance"),
                  path('teacher_apply_leave', TeacherViews.teacher_apply_leave, name="teacher_apply_leave"),
                  path('teacher_apply_leave_save', TeacherViews.teacher_apply_leave_save,name="teacher_apply_leave_save"),
                  path('teacher_feedback', TeacherViews.teacher_feedback, name="teacher_feedback"),
                  path('teacher_feedback_save', TeacherViews.teacher_feedback_save, name="teacher_feedback_save"),

                  # path('teacher_profile', TeacherViews.teacher_profile, name="teacher_profile"),
                  # path('teacher_profile_save', TeacherViews.teacher_profile_save, name="teacher_profile_save"),

                  path('get_students', TeacherViews.get_students, name="get_students"),
                  path('get_attendance_dates', TeacherViews.get_attendance_dates, name="get_attendance_dates"),
                  path('get_attendance_student', TeacherViews.get_attendance_student, name="get_attendance_student"),
                  path('save_attendance_data', TeacherViews.save_attendance_data, name="save_attendance_data"),
                  path('save_update_attendance_data', TeacherViews.save_update_attendance_data, name="save_update_attendance_data"),

                  # path('staff_fcmtoken_save', StaffViews.staff_fcmtoken_save, name="staff_fcmtoken_save"),
                  # path('staff_all_notification', StaffViews.staff_all_notification, name="staff_all_notification"),
                  # path('staff_add_result', StaffViews.staff_add_result, name="staff_add_result"),
                  # path('save_student_result', StaffViews.save_student_result, name="save_student_result"),
                  # path('edit_student_result', EditResultViewClass.as_view(), name="edit_student_result"),
                  # path('fetch_result_student', StaffViews.fetch_result_student, name="fetch_result_student"),



                  # Student URL Path
                  path('student_home', StudentViews.student_home, name="student_home"),


                  # Student Service Staff URL Path
                  path('studentservicestaff_home', StudentServiceStaffViews.studentservicestaff_home,
                       name="studentservicestaff_home")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
