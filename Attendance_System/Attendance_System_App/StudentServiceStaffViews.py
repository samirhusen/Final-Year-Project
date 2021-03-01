from django.shortcuts import render


def studentservicestaff_home(request):
    return render(request,"studentservicestaff_template/studentservicestaff_home_template.html")