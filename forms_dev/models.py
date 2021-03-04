from django.db import models

# Create your models here.
class RequestForm(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    verify_email = models.EmailField()
    text = models.CharField(max_length=100)
