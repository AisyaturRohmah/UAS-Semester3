from django.db import models

# Create your models here.

class blouse(models.Model):
     category = models.CharField(max_length=100)
     size = models.IntegerField()
     price = models.IntegerField()

     def __str__(self):
        return "{}" . format(self.category)

     