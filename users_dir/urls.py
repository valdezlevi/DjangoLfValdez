from django.urls import path
from . import views

urlpatterns = [
    path("", views.users, name="users"),
    path("other/", views.other, name="other"),

]