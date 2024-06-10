from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    dateOfBirth = models.DateField()


    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.age} anos'