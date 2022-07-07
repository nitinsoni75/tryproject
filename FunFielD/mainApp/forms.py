from dataclasses import field

from django import forms

from django.contrib.auth.models import User

from mainApp.models import Profile,Post,Follower,Following,Comment


# User registration from

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(max_length=200,help_text='Required field')

    class meta:

        model = User

        fields = ['username','email','password']




# update email


class UpdateUserForm(forms.ModelForm):
    
    email = forms.EmailField(max_length=200,help_text='Required field')

    class Meta:

        model = User

        fields = ['email']


# update profile

class UdateProfileForm(forms.ModelForm):
    class Meta:

        model = Profile

        fields = ['status_info','profile_pic']




# create a post

class CreatePost(forms.ModelForm):

    class Meta:
        model = Post

        fields  =['post_text','post_picture']
    



# create a comment

class CreateComment(forms.ModelForm):

    class Meta:
        model = Comment

        fields = ['comment_text']


