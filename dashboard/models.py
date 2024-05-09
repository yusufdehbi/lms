from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    date_of_hire = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    