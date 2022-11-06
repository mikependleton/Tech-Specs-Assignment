from django import forms
from .models import file_load


class view_Form(forms.ModelForm):
    class Meta:
        model = file_load
        fields = ["upload_file"]
