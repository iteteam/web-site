from django import forms

from app.models import *


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'image', 'theme', 'about']
