from django.db import models

# Create your models here.
class post(models.Model):
    idcheck=models.IntegerField()
    Subject=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    Description=models.TextField(max_length=300)   

    def __str__(self) :
        return self.Subject