from django.db import models

# Create your models here.

class TaskStoreModel(models.Model):
    OPTIONS = (
        ('Complete', 'Complete'),
        ('Incomplete','Incomplete'),
       
    )
  
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=20,choices=OPTIONS)
    
   
    
