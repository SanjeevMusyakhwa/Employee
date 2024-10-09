from django.db import models

# Create your models here.
class Employee(models.Model):
  name = models.CharField(max_length=20)
  email = models.EmailField()
  address = models.CharField(max_length=150)
  phone_number = models.IntegerField()

  def __str__(self):
    return self.name
