from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from Attendance_System_App.models import CustomUser, StudentServiceStaffs


def studentservicestaff_home(request):
    return render(request,"studentservicestaff_template/studentservicestaff_home_template.html")


def studentservicestaff_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    studentservicestaff=StudentServiceStaffs.objects.get(admin=user)
    return render(request,"studentservicestaff_template/studentservicestaff_profile.html",{"user":user,"studentservicestaff":studentservicestaff})

def studentservicestaff_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("studentservicestaff_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        address=request.POST.get("address")
        password=request.POST.get("password")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            if password!=None and password!="":
                customuser.set_password(password)
            customuser.save()

            studentservicestaff=StudentServiceStaffs.objects.get(admin=customuser.id)
            studentservicestaff.address=address
            studentservicestaff.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("studentservicestaff_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("studentservicestaff_profile"))