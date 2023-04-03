from django.db import models

# Create your models here.

class Datos(models.Model):
     nombre= models.CharField(max_length=20)
     numero=models.IntegerField(30)
     dni=models.IntegerField(30)
     cp=models.IntegerField(30)
     mensaje=models.TextField(blank=True)

     def __str__(self):

        return self.nombre

