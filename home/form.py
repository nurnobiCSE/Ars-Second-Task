from django import forms
from .models import create_post

class ImageForm(forms.ModelForm):
    class Meta:
        model =create_post
        fields =("text","upload","feelings","places")