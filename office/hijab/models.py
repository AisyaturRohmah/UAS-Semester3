from django.db import models

# Create your models here.

class hijab(models.Model):
     warna = models.CharField(max_length=100)
     size = models.CharField(max_length=5)
     price = models.CharField(max_length= 10)
     def __str__(self):
        return "{}". format(self.warna)