from rest_framework import serializers
from .models import Student  # make sure this import is correct

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 
