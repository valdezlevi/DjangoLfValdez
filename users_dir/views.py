from django.shortcuts import render
from users_dir.models import Users
from users_dir.forms import UserForms
# Create your views here.
# def users(request):
#     users_list = Users.objects.all()
#     users_dict = {'users_listahan' :users_list}
#     return render(request, 'usersprof/users.html', context=users_dict)

def welcome(request):
    users_list = Users.objects.all()
    users_dict = {'users_listahan' :users_list}
    return render(request, 'signupprof/welcomesignup.html', context=users_dict)

def users(request):

    form = UserForms()

    if request.method == 'POST':
        form = UserForms(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return welcome(request)

        else:
            print("ERROR FROM INVALID")
    return render(request, 'signupprof/signup.html', {'form': form})


def other(request):
    
    return render(request, 'indexprof/other.html')