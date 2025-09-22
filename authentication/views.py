from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.edit import CreateView, UpdateView

from .models import Student, Teacher, Contact, Stream
from .forms import CourseForm
from .models import Course
from django.db import models
from .models import Review


# ================== BASIC VIEWS ==================
def show(request):
    return render(request, "home.html")


def about(request):
    return render(request, 'about.html')


def mathematics(request):
    return render(request, 'mathematics.html')


def biology(request):
    return render(request, 'biology.html')


def commerce(request):
    levels = ["Beginner", "Intermediate", "Advanced"]
    return render(request, "commerce.html", {"levels": levels})


def arts(request):
    return render(request, 'arts.html')


# ================== STUDENT CRUD ==================
def all_stu(request):
    students = Student.objects.all()
    return render(request, 'viewstudent.html', {'studs': students})


def register(request):
    if request.method == 'POST':
        student = Student(
            s_name=request.POST.get('s_name'),
            s_fathername=request.POST.get('s_fathername'),
            s_mothername=request.POST.get('s_mothername'),
            s_addr=request.POST.get('s_addr'),
            s_school=request.POST.get('s_school'),
            s_contactnumber=request.POST.get('s_contactnumber'),
            s_email=request.POST.get('s_email'),
            s_gender=request.POST.get('s_gender'),
            s_class=request.POST.get('s_class')
        )
        student.save()
        messages.success(request, "Student has been added successfully")
        return redirect('reg')

    return render(request, 'register.html')


def delete_stud(request, stud_id=None):
    if stud_id:
        student = get_object_or_404(Student, id=stud_id)
        student.delete()
        messages.success(request, "Student has been deleted successfully")
        return redirect('delete_stud')

    students = Student.objects.all()
    return render(request, 'delete_student.html', {'studs': students})


def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.course = request.POST.get("course")
        student.save()
        return redirect("all_stu")

    return render(request, "update_student.html", {"student": student})


# ================== TEACHER CRUD ==================
def teacher_register(request):
    if request.method == "POST":
        email = request.POST.get('email')

        if Teacher.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('teacher_register')

        teacher = Teacher(
            name=request.POST.get('name'),
            email=email,
            phone=request.POST.get('phone'),
            department=request.POST.get('department'),
            password=make_password(request.POST.get('password'))
        )
        teacher.save()
        messages.success(request, "Teacher registered successfully!")
        return redirect('teacher_register')

    return render(request, 'teacher_register.html')


# ================== CONTACT FORM ==================
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        # Optional email notification
        send_mail(
            subject=f"New Contact Form Submission: {subject}",
            message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=True,
        )
        return render(request, "contactus.html", {"success": "Your message has been sent!"})

    return render(request, "contactus.html")


# ================== COURSES ==================
def courses_view(request):
    streams = Stream.objects.prefetch_related("subjects").all()
    return render(request, "courses.html", {"streams": streams})


def course_list(request):
    streams = Stream.objects.prefetch_related("subjects__courses").all()
    return render(request, "courses.html", {"streams": streams})

def course_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        duration = request.POST.get("duration")
        Course.objects.create(name=name, description=description, duration=duration)
        return redirect("course_list")
    return render(request, "course_form.html")

def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("course_list")  # ya jaha redirect karna ho
    else:
        form = CourseForm(instance=course)
    return render(request, "course_form.html", {"form": form})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.delete()
        return redirect("course_list")
    return render(request, "courses/course_confirm_delete.html", {"course": course})

def submit_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

    return render(request, 'thank_you.html')

def reviews_page(request):
    # Fetch only approved reviews
    approved_reviews = Review.objects.filter(approved=True)
    
    context = {
        'reviews': approved_reviews
    }
    return render(request, 'reviews_page.html', context)

def thank_you_view(request):
    return render(request, 'thank_you.html')


# ================== CLASS BASED VIEWS ==================
class StudentView(CreateView):
    model = Student
    fields = ["s_name", "s_fathername", "s_mothername", "s_addr", "s_school",
              "s_contactnumber", "s_email", "s_gender", "s_class"]
    template_name = "student_form.html"
    success_url = "/all_stu/"


class StudentUpdateView(UpdateView):
    model = Student
    fields = ["s_name", "s_fathername", "s_mothername", "s_addr", "s_school",
              "s_contactnumber", "s_email", "s_gender", "s_class"]
    template_name = "student_form.html"
    success_url = "/all_stu/"

