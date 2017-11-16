from django import forms
from django.contrib.auth.models import User

from .models import Student,Teacher,Group,Course

class CreateFormStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "name",
            "surname",
            "image",
            "bio",
         ]


class CreateFormTeacher(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            "name",
            "surname",
            "image",
            "bio",
            "courser"
         ]


class CreateFormGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            "title",
            "course",
            "the_elder",
            "students",
         ]

class CreateFormCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
           "info",
           "teacher"
            "student"
         ]