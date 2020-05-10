from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label="Email Address")
    reenter_email = forms.EmailField(label="Verify Email")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email1 = all_clean_data['email']
        email2 = all_clean_data['reenter_email']

        if email1 != email2:
            raise forms.ValidationError("Emails mismatch")