from django.contrib import admin
from .models import Student, Teacher, Contact, Stream, Subject, Course, Review


# ------------------------------
# Student
# ------------------------------
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "s_name", "s_fathername", "s_email", "s_contactnumber", "s_class")
    search_fields = ("s_name", "s_email", "s_contactnumber")
    list_filter = ("s_class", "s_gender")


# ------------------------------
# Teacher
# ------------------------------
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone", "department")
    search_fields = ("name", "email", "department")


# ------------------------------
# Contact
# ------------------------------
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")
    list_filter = ("created_at",)


# ------------------------------
# Course
# ------------------------------
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "subject", "fee", "duration")
    search_fields = ("name",)
    list_filter = ("subject",)

# ------------------------------
# Subject
# ------------------------------
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "stream")
    search_fields = ("name",)
    list_filter = ("stream",)

# ------------------------------
# reviw
# ------------------------------
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rating', 'approved', 'created_at')
    list_filter = ('approved', 'created_at', 'rating')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected reviews have been approved!")
    approve_reviews.short_description = "Approve selected reviews"