from django.db import models

# Create your models here.

class CsvFile(models.Model):
    file=models.FileField(upload_to='files/')
    created_at=models.DateTimeField(auto_now_add=True)

class FileDetails(models.Model):
    first_name=models.CharField(max_length=50,blank=True,null=True) 
    last_name=models.CharField(max_length=50,blank=True,null=True)    
    gender=models.CharField(max_length=30,blank=True,null=True) 
    email=models.EmailField(max_length=100,blank=True,null=True)   
    phone=models.IntegerField(blank=True,null=True)
   
    def __str__(self):
        return f"{self.first_name}"
    
    