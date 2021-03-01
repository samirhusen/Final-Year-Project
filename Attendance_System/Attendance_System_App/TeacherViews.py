from django.shortcuts import render


def teacher_home(request):
    return render(request,"teacher_template/teacher_home_template.html")