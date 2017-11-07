from django import forms
from django.contrib.auth.models import User

from .models import Profesor



class PostForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = [
            "name",
            " midlename",
            "surname",
            "image",
            "bio",
            "courser",

         ]
