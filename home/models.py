from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings
from django.conf.urls.static import static
from django.forms import ModelForm
from django import forms

class Upload(models.Model):
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    applicat_name=models.CharField(max_length=50,blank=True,null=True)

    gender=models.CharField(max_length=10,blank=True,null=True)
    email=models.EmailField(max_length=50,null=True)
    contact_number=models.DecimalField(max_digits=15,decimal_places=0,blank=False,null=True)
    upload = models.ImageField(upload_to='usermedia',null=True,blank=True)

    def __str__(self):
     return self.applicat_name






class gallary(models.Model):
    tittle=models.CharField(max_length = 30)
    url = models.URLField(blank=True)
    description = models.CharField(max_length=500)
    date=models.DateField(blank=False)
    image = models.ImageField(upload_to='Media')
