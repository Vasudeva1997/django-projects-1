from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper


def setAttrs(attrType, placeholder, **kwargs):
    tempAttrs = {'class': 'form-control col-lg-5',
                 'type': attrType, 'placeholder': placeholder}
    if kwargs:
        for key, value in kwargs.items():
            tempAttrs[key] = value
        return tempAttrs
    else:
        return tempAttrs


class NewPostForm(forms.ModelForm):
    class Meta():
        model = models.Post
        fields = ['title', "description","image_file"]
        widgets = {
            'title': forms.TextInput(
                attrs=setAttrs('text', 'Enter Title')
            ),
            'description': forms.Textarea(
                attrs=setAttrs(
                    'textarea', 'Enter few words . . . . . .', rows="5")
            )
        }


class CommentForm(forms.ModelForm):
    class Meta():
        model = models.Comment
        fields = ['author', 'comment']
        widgets = {
            'author': forms.TextInput(
                attrs=setAttrs('text', 'Your Name')
            ),
            'comment': forms.Textarea(
                attrs=setAttrs('textarea','Enter Comment',rows=2)
            )
        }


class SignUpForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username','first_name', 'last_name','email' )
        widgets = {
            'username':forms.TextInput(attrs=setAttrs("text","Username")),
            'first_name': forms.TextInput(attrs=setAttrs("text","First Name")),
            'last_name':  forms.TextInput(attrs=setAttrs("text","Last Name")),
            'email' :  forms.EmailInput(attrs=setAttrs("email","Your Email ID")),
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs = setAttrs("password","Password")
        self.fields['password2'].widget.attrs = setAttrs("password","Re-enter Password")