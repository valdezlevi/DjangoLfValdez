from django.shortcuts import render
from . import forms
from forms_dev.models import RequestForm
# Create your views here.
def welcome(request):
    access_list = RequestForm.objects.all()
    access_dict = {'access_listahan' :access_list}
    return render(request, 'formprof/welcome.html', context=access_dict)

def forms_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form=forms.FormName(request.POST)

        if form.is_valid():
            print("NAME:" +form.cleaned_data['name'])
            print("EMAIL:" +form.cleaned_data['email'])
            print("VERIFY EMAIL:" +form.cleaned_data['verify_email'])
            print("TEXT:" +form.cleaned_data['text'])
            return welcome(request)

    return render(request, 'formprof/form.html', {'form': form}) 