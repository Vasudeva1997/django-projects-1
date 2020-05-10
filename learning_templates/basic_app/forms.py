from django.contrib.auth.models import User
from basic_app.models import UserProfile
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfo(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('portfolio_site','profile_pic')
