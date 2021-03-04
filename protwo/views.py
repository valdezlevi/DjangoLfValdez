from django.shortcuts import render
# Create your views here.
def help(request):
    my_dict = {'ako_help': "hi ako si view.py ni help"}
    return render(request, 'helpprof/help.html', context=my_dict)