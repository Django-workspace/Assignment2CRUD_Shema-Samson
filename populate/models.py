from pyexpat import model
from xmlrpc.client import DateTime
from django.db import models
from django.db import connections

# Create your models here.

class assignment1(models.Model):
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    regDate=models.DateTimeField(auto_now_add=True)

class retrievedata(models.Model):
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    regDate=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="populate_assignment1"
        managed=False