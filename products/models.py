from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) # max_length is required
    description = models.TextField(blank=True, null = True) # null has to do with database (empty in the database)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    summary = models.TextField(blank=True, null=False) # blank makes fields required or not 
    featured = models.BooleanField() # null = True or default = True