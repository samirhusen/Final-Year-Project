from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from Attendance_System_App.models import Subjects, SessionYearModel
from Attendance_System_App.models import Teachers, LeaveReportTeachers, FeedBackTeachers
from django.urls import reverse


def teacher_home(request):
    return render(request, "teacher_template/teacher_home_template.html")


def teacher_take_attendance(request):
    subjects = Subjects.objects.filter(teacher_id=request.user.id)
    session_years = SessionYearModel.object.all()
    return render(request, "teacher_template/teacher_take_attendance.html",
                  {"subjects": subjects, "session_years": session_years})


def teacher_update_attendance(request):
    subjects = Subjects.objects.filter(teacher_id=request.user.id)
    session_years = SessionYearModel.object.all()
    return render(request, "teacher_template/teacher_update_attendance.html",
                  {"subjects": subjects, "session_years": session_years})


def teacher_apply_leave(request):
    teacher_obj = Teachers.objects.get(admin=request.user.id)
    leave_data = LeaveReportTeachers.objects.filter(teacher_id=teacher_obj)
    return render(request, "teacher_template/teacher_apply_leave.html", {"leave_data": leave_data})


def teacher_apply_leave_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("teacher_apply_leave"))
    else:
        leave_date = request.POST.get("leave_date")
        leave_msg = request.POST.get("leave_msg")

        teacher_obj = Teachers.objects.get(admin=request.user.id)
        try:
            leave_report = LeaveReportTeachers(teacher_id=teacher_obj, leave_date=leave_date, leave_message=leave_msg,
                                               leave_status=0)
            leave_report.save()
            messages.success(request, "Successfully Applied for Leave")
            return HttpResponseRedirect(reverse("teacher_apply_leave"))
        except:
            messages.error(request, "Failed To Apply for Leave")
            return HttpResponseRedirect(reverse("teacher_apply_leave"))


def teacher_feedback(request):
    teacher_id = Teachers.objects.get(admin=request.user.id)
    feedback_data = FeedBackTeachers.objects.filter(teacher_id=teacher_id)
    return render(request, "teacher_template/teacher_feedback.html", {"feedback_data": feedback_data})


def teacher_feedback_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("teacher_feedback_save"))
    else:
        feedback_msg = request.POST.get("feedback_msg")

        teacher_obj = Teachers.objects.get(admin=request.user.id)
        try:
            feedback = FeedBackTeachers(teacher_id=teacher_obj, feedback=feedback_msg, feedback_reply="")
            feedback.save()
            messages.success(request, "Successfully Sent Feedback")
            return HttpResponseRedirect(reverse("teacher_feedback"))
        except:
            messages.error(request, "Failed To Send Feedback")
            return HttpResponseRedirect(reverse("teacher_feedback"))
