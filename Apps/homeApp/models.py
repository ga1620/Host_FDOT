from django.db import models

# Create your models here.
class DataFileUpload(models.Model):
    file_name = models.CharField(max_length=50)
    actual_file = models.FileField(upload_to ='uploads/')
    description = models.CharField(max_length=400,null=True,blank=True)
    
    def __str__(self):
        return self.file_name

# create database
class WebsiteAuth(models.Model):
    webname = models.CharField(max_length=100)
    status = models.BooleanField()       