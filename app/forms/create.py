from django import forms
from django.contrib.auth.forms import UserCreationForm

from app.models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['about', 'image', 'theme']


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'about', 'description', 'image']


class LectureCreationForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['course', 'title', 'about', 'file']


class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'post', 'content']


class GenericQuestionAnswerCreationForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['user', 'question', 'content']
