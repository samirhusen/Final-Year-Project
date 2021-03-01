from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from Attendance_System_App.forms import AddStudentForm, EditStudentForm
from Attendance_System_App.models import CustomUser, Courses, Subjects, Teachers, Students, StudentServiceStaffs


def admin_home(request):
    return render(request, "admin_template/home_content.html")


def add_teacher(request):
    return render(request, "admin_template/add_teacher_template.html")


def add_teacher_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  last_name=last_name, first_name=first_name, user_type=2)
            user.teachers.address = address
            user.save()
            messages.success(request, "Teacher Successfully Added")
            return HttpResponseRedirect(reverse("add_teacher"))
        except:
            messages.error(request, "Failed to Add Teacher")
            return HttpResponseRedirect(reverse("add_teacher"))


def add_student_service_staff(request):
    return render(request, "admin_template/add_student_service_staff_template.html")

def add_student_service_staff_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  last_name=last_name, first_name=first_name, user_type=3)
            user.studentservicestaffs.address = address
            user.save()
            messages.success(request, "Student Service Staff Successfully Added")
            return HttpResponseRedirect(reverse("add_student_service_staff"))
        except:
            messages.error(request, "Failed to Add Student Service Staff")
            return HttpResponseRedirect(reverse("add_student_service_staff"))


def add_course(request):
    return render(request, "admin_template/add_course_template.html")

def add_course_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        course = request.POST.get("course")
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, "Course Successfully Added")
            return HttpResponseRedirect(reverse("add_course"))
        except:
            messages.error(request, "Failed To Add Course")
            return HttpResponseRedirect(reverse("add_course"))


def add_student(request):
    form=AddStudentForm()
    return render(request,"admin_template/add_student_template.html",{"form":form})

def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddStudentForm(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            address=form.cleaned_data["address"]
            session_start=form.cleaned_data["session_start"]
            session_end=form.cleaned_data["session_end"]
            course_id=form.cleaned_data["course"]
            sex=form.cleaned_data["sex"]

            profile_pic=request.FILES['profile_pic']
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url=fs.url(filename)

            try:
                user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,
                                                    first_name=first_name,user_type=4)
                user.students.address=address
                course_obj=Courses.objects.get(id=course_id)
                user.students.course_id=course_obj
                user.students.session_start_year=session_start
                user.students.session_end_year=session_end
                user.students.gender=sex
                user.students.profile_pic=profile_pic_url
                user.save()
                messages.success(request,"Successfully Added Student")
                return HttpResponseRedirect(reverse("add_student"))
            except:
                messages.error(request,"Failed to Add Student")
                return HttpResponseRedirect(reverse("add_student"))
        else:
            form=AddStudentForm(request.POST)
            return render(request, "admin_template/add_student_template.html", {"form": form})

def add_subject(request):
    courses=Courses.objects.all()
    teachers=CustomUser.objects.filter(user_type=2)
    return render(request,"admin_template/add_subject_template.html",{"teachers":teachers,"courses":courses})

def add_subject_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_name=request.POST.get("subject_name")
        course_id=request.POST.get("course")
        course=Courses.objects.get(id=course_id)
        teacher_id=request.POST.get("teacher")
        teacher=CustomUser.objects.get(id=teacher_id)

        try:
            subject=Subjects(subject_name=subject_name,course_id=course,teacher_id=teacher)
            subject.save()
            messages.success(request,"Subject Successfully Added")
            return HttpResponseRedirect(reverse("add_subject"))
        except:
            messages.error(request,"Failed to Add Subject")
            return HttpResponseRedirect(reverse("add_subject"))

def manage_teacher(request):
    teachers=Teachers.objects.all()
    return render(request,"admin_template/manage_teacher_template.html",{"teachers":teachers})

def manage_student(request):
    students=Students.objects.all()
    return render(request,"admin_template/manage_student_template.html",{"students":students})

def manage_student_service_staff(request):
    studentservicestaffs=StudentServiceStaffs.objects.all()
    return render(request,"admin_template/manage_student_service_staff_template.html",{"studentservicestaffs":studentservicestaffs})

def manage_course(request):
    courses=Courses.objects.all()
    return render(request,"admin_template/manage_course_template.html",{"courses":courses})

def manage_subject(request):
    subjects=Subjects.objects.all()
    return render(request,"admin_template/manage_subject_template.html",{"subjects":subjects})

# Teacher
def edit_teacher(request,teacher_id):
    teacher=Teachers.objects.get(admin=teacher_id)
    return render(request,"admin_template/edit_teacher_template.html",{"teacher":teacher,"id":teacher_id})

def edit_teacher_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        teacher_id=request.POST.get("teacher_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        address=request.POST.get("address")

        try:
            user=CustomUser.objects.get(id=teacher_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()
            teacher_model=Teachers.objects.get(admin=teacher_id)
            teacher_model.address=address
            teacher_model.save()
            messages.success(request,"Successfully Edited Teacher")
            return HttpResponseRedirect(reverse("edit_teacher",kwargs={"teacher_id":teacher_id}))
        except:
            messages.error(request,"Failed to Edit Teacher")
            return HttpResponseRedirect(reverse("edit_teacher",kwargs={"teacher_id":teacher_id}))


def edit_student_service_staff(request,studentservicestaff_id):
    studentservicestaff=StudentServiceStaffs.objects.get(admin=studentservicestaff_id)
    return render(request,"admin_template/edit_student_service_staff_template.html",{"studentservicestaff":studentservicestaff,"id":studentservicestaff_id})

def edit_student_service_staff_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        studentservicestaff_id=request.POST.get("studentservicestaff_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        address=request.POST.get("address")

        try:
            user=CustomUser.objects.get(id=studentservicestaff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()
            studentservicestaff_model=StudentServiceStaffs.objects.get(admin=studentservicestaff_id)
            studentservicestaff_model.address=address
            studentservicestaff_model.save()
            messages.success(request,"Successfully Edited Student Service Staff")
            return HttpResponseRedirect(reverse("edit_student_service_staff",kwargs={"studentservicestaff_id":studentservicestaff_id}))
        except:
            messages.error(request,"Failed to Edit Student Service Staff")
            return HttpResponseRedirect(reverse("edit_student_service_staff",kwargs={"studentservicestaff_id":studentservicestaff_id}))

def edit_student(request,student_id):
    request.session['student_id']=student_id
    student=Students.objects.get(admin=student_id)
    form=EditStudentForm()
    form.fields['email'].initial=student.admin.email
    form.fields['first_name'].initial=student.admin.first_name
    form.fields['last_name'].initial=student.admin.last_name
    form.fields['username'].initial=student.admin.username
    form.fields['address'].initial=student.address
    form.fields['course'].initial=student.course_id.id
    form.fields['sex'].initial=student.gender
    form.fields['session_start'].initial=student.session_start_year
    form.fields['session_end'].initial=student.session_end_year
    return render(request,"admin_template/edit_student_template.html",{"form":form,"id":student_id,"username":student.admin.username})

def edit_student_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        student_id=request.session.get("student_id")
        if student_id==None:
            return HttpResponseRedirect(reverse("manage_student"))

        form=EditStudentForm(request.POST,request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]
            session_start = form.cleaned_data["session_start"]
            session_end = form.cleaned_data["session_end"]
            course_id = form.cleaned_data["course"]
            sex = form.cleaned_data["sex"]

            if request.FILES.get('profile_pic',False):
                profile_pic=request.FILES['profile_pic']
                fs=FileSystemStorage()
                filename=fs.save(profile_pic.name,profile_pic)
                profile_pic_url=fs.url(filename)
            else:
                profile_pic_url=None


            try:
                user=CustomUser.objects.get(id=student_id)
                user.first_name=first_name
                user.last_name=last_name
                user.username=username
                user.email=email
                user.save()

                student=Students.objects.get(admin=student_id)
                student.address=address
                student.session_start_year=session_start
                student.session_end_year=session_end
                student.gender=sex
                course=Courses.objects.get(id=course_id)
                student.course_id=course
                if profile_pic_url!=None:
                    student.profile_pic=profile_pic_url
                student.save()
                del request.session['student_id']
                messages.success(request,"Successfully Edited Student")
                return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id}))
            except:
                messages.error(request,"Failed to Edit Student")
                return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id}))
        else:
            form=EditStudentForm(request.POST)
            student=Students.objects.get(admin=student_id)
            return render(request,"admin_template/edit_student_template.html",{"form":form,"id":student_id,"username":student.admin.username})


def edit_subject(request,subject_id):
    subject=Subjects.objects.get(id=subject_id)
    courses=Courses.objects.all()
    teachers=CustomUser.objects.filter(user_type=2)
    return render(request,"admin_template/edit_subject_template.html",{"subject":subject,"teachers":teachers,"courses":courses,"id":subject_id})

def edit_subject_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_id=request.POST.get("subject_id")
        subject_name=request.POST.get("subject_name")
        teacher_id=request.POST.get("teacher")
        course_id=request.POST.get("course")

        try:
            subject=Subjects.objects.get(id=subject_id)
            subject.subject_name=subject_name
            teacher=CustomUser.objects.get(id=teacher_id)
            subject.teacher_id=teacher
            course=Courses.objects.get(id=course_id)
            subject.course_id=course
            subject.save()

            messages.success(request, "Successfully Edited Subject")
            return HttpResponseRedirect(reverse("edit_subject", kwargs={"subject_id": subject_id}))
        except:
            messages.error(request, "Failed to Edit Subject")
            return HttpResponseRedirect(reverse("edit_subject", kwargs={"subject_id": subject_id}))


def edit_course(request,course_id):
    course=Courses.objects.get(id=course_id)
    return render(request,"admin_template/edit_course_template.html",{"course":course,"id":course_id})

def edit_course_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        course_id=request.POST.get("course_id")
        course_name=request.POST.get("course")

        try:
            course=Courses.objects.get(id=course_id)
            course.course_name=course_name
            course.save()
            messages.success(request, "Successfully Edited Course")
            return HttpResponseRedirect(reverse("edit_course", kwargs={"course_id": course_id}))
        except:
            messages.error(request, "Failed to Edit Course")
            return HttpResponseRedirect(reverse("edit_course", kwargs={"course_id": course_id}))