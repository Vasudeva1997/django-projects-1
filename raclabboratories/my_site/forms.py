from django import forms
from . import models

def setAttrs(placeholder,classname = 'form-control col-lg-8',type2="text",**kwargs):
    attrs = {'class':classname,'type':type2,'placeholder':placeholder}
    if kwargs:
        for key,value in kwargs.items():
            attrs[key] = value
    return attrs


class PostForm(forms.ModelForm):
    class Meta():
        model = models.Post
        fields = ('impurity_name','cas_no','quantity','current_price','actual_price','image_file')

        widgets = {
            'impurity_name':forms.TextInput(attrs=setAttrs(placeholder='Impurity Name')),
            'cas_no' : forms.TextInput(attrs=setAttrs(placeholder='CAS Number')),
        }

class OrderForm(forms.ModelForm):
    class Meta():
        model = models.Order
        fields = ('name','email','mobile','place','description')

        widgets = {
            'name':forms.TextInput(attrs=setAttrs(placeholder='Full Name')),
            'place' : forms.TextInput(attrs=setAttrs(placeholder='Your Place')),
            'description':forms.Textarea(attrs=setAttrs(placeholder='Any Other queires....',rows="3")),
        }