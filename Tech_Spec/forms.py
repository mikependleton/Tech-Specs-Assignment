from django import forms
from .models import file_load
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class view_Form(forms.ModelForm):
    class Meta:
        model = file_load
        fields = ["upload_file"]


class read_Form(forms.Form):
    read_lines = forms.Textarea


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
