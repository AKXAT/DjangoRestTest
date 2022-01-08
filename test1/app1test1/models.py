from django.db import models

# Create your models here.
class Cities(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=3)
    utilities = models.CharField(max_length=300)