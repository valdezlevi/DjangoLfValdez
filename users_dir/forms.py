from django import forms
from users_dir.models import Users

class UserForms(forms.ModelForm):
    class Meta():
        model = Users
        fields = '__all__'