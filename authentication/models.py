from django.db import models
from django.contrib.auth.models import User


# ------------------------------
# Student
# ------------------------------
class Student(models.Model):
    s_name = models.CharField(max_length=200, verbose_name="Student Name")
    s_fathername = models.CharField(max_length=200, verbose_name="Father's Name")
    s_mothername = models.CharField(max_length=200, verbose_name="Mother's Name")
    s_addr = models.CharField(max_length=200, verbose_name="Address")
    s_school = models.CharField(max_length=200, verbose_name="School Name")
    s_contactnumber = models.CharField(max_length=15, default="9999999999", verbose_name="Contact Number")
    s_email = models.EmailField(max_length=200, unique=True, verbose_name="Email")
    s_gender = models.CharField(
        max_length=10,
        choices=(("Male", "Male"), ("Female", "Female")),
        verbose_name="Gender"
    )
    s_class = models.CharField(max_length=200, verbose_name="Class")

    def __str__(self):
        return f"{self.s_name} ({self.s_email})"


# ------------------------------
# Teacher
# ------------------------------
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    password = models.CharField(max_length=256)  # Suggestion: Django User Model use karo

    def __str__(self):
        return self.name


# ------------------------------
# Contact
# ------------------------------
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


# ------------------------------
# Stream (Mathematics, Biology, etc.)
# ------------------------------
class Stream(models.Model):
    name = models.CharField(max_length=100)

# ------------------------------
# Subject (Maths, Physics, etc.)
# ------------------------------
class Subject(models.Model):
    name = models.CharField(max_length=100)
    stream = models.ForeignKey(Stream, default=1, on_delete=models.CASCADE)
# ------------------------------
# Course (with Fee + Duration)
# ------------------------------
class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="courses")
    name = models.CharField(max_length=100)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50, blank=True, null=True, verbose_name="Duration (e.g. 6 months)")

    def __str__(self):
        return f"{self.name} - {self.subject.name}"
    
# ------------------------------
# review
# ------------------------------

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
