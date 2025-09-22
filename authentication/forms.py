from django import forms
from .models import Stream, Subject, Course, Review


class StreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields = ['name']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['stream', 'name']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['subject', 'name', 'fee', 'duration']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'comment', 'rating']  # message → comment
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Write your review here...'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }