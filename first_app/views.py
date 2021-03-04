from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage
# Create your views here.
def index (request):
    return render(request, 'indexprof/index.html')

def webrecord(request):
    #eto ung code to display the Database
    webpages_list = AccessRecord.objects.all()
    date_dict = {'access_records' :webpages_list}
    return render(request, 'indexprof/webrecord.html', context=date_dict)