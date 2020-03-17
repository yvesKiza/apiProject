from rest_framework import serializers
import uuid 
from .models import hospital



class hospitalSerializer(serializers.Serializer):
   name=serializers.CharField(max_length=50,blank=False)
   email=serializers.EmailField(max_length=70, null=True, blank=True, unique=True)
   key=serializers.UUIDField(default=uuid.uuid4, editable=False,unique=True)   
   joined=serializers.DateTimeField(auto_now=True)
   number_test=serializers.BigIntegerField(default=0) 

    
def create(self, validated_data):
        return hospital.objects.create(validated_data)
    
def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.email=validated_data.get('email',instance.email)
          
        instance.save()
        return instance