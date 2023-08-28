from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    desc = models.TextField()
    
    def __str__(self):
        return self.name