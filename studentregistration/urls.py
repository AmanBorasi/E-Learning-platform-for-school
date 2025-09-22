from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', views.show, name="home"),

    # About
    path('about/', views.about, name='about'),
    path('submit-review/', views.submit_review, name='submit_review'),
    path('thank-you/', views.thank_you_view, name='thank_you'),

    # Student
    path('student_login/', views.register, name='student_login'),
    path('student/all/', views.all_stu, name='all_stu'),
    path('student/delete/<int:stud_id>/', views.delete_stud, name='delete_stud'),
    path('student/update/<int:id>/', views.update_student, name='update_student'),
    path('student/create/', views.StudentView.as_view(), name='student_create'),

    # Teacher
    path('teacher_login/', views.teacher_register, name='teacher_register'),

    # Contact
    path("contact/", views.contact_view, name="contact"),

    # Courses
    path("courses/", views.course_list, name="course_list"),
    path("courses/create/", views.course_create, name="course_create"),
    path("courses/<int:pk>/update/", views.course_update, name="course_update"),
    path("courses/<int:pk>/delete/", views.course_delete, name="course_delete"),

    # Streams
    path('courses/biology/', views.biology, name='biology'),
    path('courses/mathematics/', views.mathematics, name='mathematics'),
    path('courses/commerce/', views.commerce, name='commerce'),
    path('courses/arts/', views.arts, name='arts'),
]

# Static & Media setup (development only)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
