from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your Email Again:")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self): #using SELF eto ung shortcut or other meaning ni class name na dapat FormName then ginawang self nalang
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")