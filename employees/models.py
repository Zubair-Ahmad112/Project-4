from django.db import models

# Creating model below.


class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    department = models.CharField(max_length=50)
    professional_exp = models.FloatField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f'Employee: {self.first_name} {self.last_name}'
