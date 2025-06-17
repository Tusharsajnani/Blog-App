from django.db import models

# Create your models here.
class Student(models.Model): #Add:- name,age,gender,email,phone_number
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField()
    email = models.CharField()
    phone_num = models.CharField(max_length=13)


    def __str__(self):
        return self.name + ' ' + self.email
