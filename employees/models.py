from django.db import models

# Creating model below.
class Employee(models.Model):
  
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  employee_number = models.PositiveIntegerField()
  email = models.EmailField(max_length=100)
  department = models.CharField(max_length=50)
  professional_exp = models.FloatField()

  def __str__(self):
    return f'Employee: {self.first_name} {self.last_name}'
  
  
  
