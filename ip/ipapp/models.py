from django.db import models

# Create your models here.

class Home(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    about = models.TextField()
    copyright = models.CharField(max_length=255,blank=True,null=True)
    name = models.CharField(max_length=255,blank=True,null=True)
    email = models.CharField(max_length=255,blank=True,null=True)
    phone = models.CharField(max_length=255,blank=True,null=True)
    

def __str__(self):
    return self.title

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    your_name = models.CharField(max_length=255,blank=True,null=True)
    your_mail = models.CharField(max_length=255,blank=True,null=True)
    your_number = models.CharField(max_length=255,blank=True,null=True)
    select_gender = models.CharField(max_length=255,blank=True,null=True)
	

def __str__(self):
     return self.your_name
		
		

	
	
	