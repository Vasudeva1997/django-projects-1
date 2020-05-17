from django import forms
from . import models


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
        fields = ['title', 'image_url', "description"]
        widgets = {
            'title': forms.TextInput(
                attrs=setAttrs('text', 'Enter Title')
            ),
            'image_url': forms.TextInput(
                attrs=setAttrs('text', 'http://www.xyz.com/img.png')
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
