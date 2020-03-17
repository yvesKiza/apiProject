from django.db import models
import uuid 
# Create your models here.
class hospital(models.Model):
   
    name=models.CharField(max_length=50,blank=False)
  
    email=models.EmailField(max_length=70, null=True, blank=True, unique=True)
    key=models.UUIDField(default=uuid.uuid4, editable=False,unique=True)   
    joined=models.DateTimeField(auto_now=True)
    number_test=models.BigIntegerField(default=0) 
    
    
    def __str__(self):
        return self.name
