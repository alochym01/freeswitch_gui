from django.db import models


# Create your models here.
class fsUser(models.Model):
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Toll_allow = models.CharField(max_length=20)
    User_context = models.CharField(max_length=20)

    def __unicode__(self):
        return self.Username
