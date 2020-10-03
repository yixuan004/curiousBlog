from django.db import models

# Create your models here.
class companyInfo(models.Model):
    companyName = models.CharField(max_length=1024)
    time = models.CharField(max_length=1024)
    companyNews = models.CharField(max_length=1024)