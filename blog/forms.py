from django import forms
from .models import (Post, Comment, ToContact, Sign_up, Profile)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('published_date','user')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('published_date','user','post')

class ToContactForm(forms.ModelForm):
    class Meta:
        model = ToContact
        fields = ('login','email')
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Sign_up
        fields = ('login','email','poster','date_of_birth')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['login', 'email', 'poster', 'date_of_birth']

