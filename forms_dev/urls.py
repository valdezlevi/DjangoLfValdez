from django.urls import path
from . import views

urlpatterns = [
    path ('', views.forms_name_view , name='forms_name_view')
]