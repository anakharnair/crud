from django.db import models
class Task(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    adress=models.CharField(max_length=250)
    photo=models.ImageField(upload_to='')
    desig=models.CharField(max_length=250)
    def __str__(self):
        return self.name
# Create your models here.