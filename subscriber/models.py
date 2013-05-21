from django.db import models


# Create your models here.
class fsUser(models.Model):
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
