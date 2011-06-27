from django.db import models

# Create your models here.
class BasicChangelist(models.Model):
    fieldA = models.CharField(max_length=100)
    fieldB = models.CharField(max_length=100)
    fieldC = models.CharField(max_length=100)
    fieldD1 = models.CharField(max_length=100, blank=True, null=True)
    fieldD2 = models.EmailField(max_length=100, blank=True, null=True)
    fieldD3 = models.TextField(max_length=100, blank=True, null=True)
