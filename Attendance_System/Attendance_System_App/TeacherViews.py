from django.shortcuts import render

from Attendance_System_App.models import Subjects, SessionYearModel


def teacher_home(request):
    return render(request, "teacher_template/teacher_home_template.html")


def teacher_take_attendance(request):
    subjects = Subjects.objects.filter(teacher_id=request.user.id)
    session_years = SessionYearModel.object.all()
    return render(request,"teacher_template/teacher_take_attendance.html",
                  {"subjects": subjects, "session_years": session_years})
