from django.db import models

# Create your models here.
class SignUpModel(models.Model):
    username = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=64)