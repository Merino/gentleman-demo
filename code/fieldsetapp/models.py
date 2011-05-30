from django.db import models

# Create your models here.
class Column(models.Model):
    column01 = models.CharField(max_length=30)
    column02 = models.CharField(max_length=30)
    
    columnA1 = models.CharField(max_length=30)
    columnA2 = models.CharField(max_length=30)
    columnA3 = models.CharField(max_length=30)
    columnA4 = models.CharField(max_length=30)
    columnA5 = models.CharField(max_length=30)
    
    columnB1 = models.CharField(max_length=30)
    columnB2 = models.CharField(max_length=30)
    columnB3 = models.CharField(max_length=30)
    columnB4 = models.CharField(max_length=30)
    columnB5 = models.CharField(max_length=30)
    
    columnC1 = models.CharField(max_length=30)
    columnC2 = models.CharField(max_length=30)
    columnC3 = models.CharField(max_length=30)
    columnC4 = models.CharField(max_length=30)
    columnC5 = models.CharField(max_length=30)
    
    columnD1 = models.CharField(max_length=30)
    columnD2 = models.CharField(max_length=30)
    columnD3 = models.CharField(max_length=30)
    columnD4 = models.CharField(max_length=30)
    columnD5 = models.CharField(max_length=30)
    
    columnE1 = models.CharField(max_length=30)
    columnE2 = models.CharField(max_length=30)
    columnE3 = models.CharField(max_length=30)
    columnE4 = models.CharField(max_length=30)
    columnE5 = models.CharField(max_length=30)
    
    columnFA1 = models.CharField(max_length=30)
    columnFB1 = models.CharField(max_length=30)
    columnFB2 = models.CharField(max_length=30)
    columnFC1 = models.CharField(max_length=30)
    columnFC2 = models.CharField(max_length=30)
    columnFC3 = models.CharField(max_length=30)
    
    columnGA1 = models.CharField(max_length=30)
    columnGB1 = models.CharField(max_length=30)
    columnGB2 = models.CharField(max_length=30)
    
    columnHA1 = models.CharField(max_length=30)
    columnHB1 = models.CharField(max_length=30)
    columnHB2 = models.CharField(max_length=30)
    
class Collapse(models.Model):
    fieldsetA1 = models.CharField(max_length=30)
    fieldsetA2 = models.CharField(max_length=30)
    fieldsetA3 = models.CharField(max_length=30)
    
    fieldsetB1 = models.CharField(max_length=30)
    fieldsetB2 = models.CharField(max_length=30)
    fieldsetB3 = models.CharField(max_length=30)
    
    fieldsetC1 = models.CharField(max_length=30)
    fieldsetC2 = models.CharField(max_length=30)
    fieldsetC3 = models.CharField(max_length=30)
    
class Action(models.Model):
    actionA1 = models.CharField(max_length=30)
    actionA2 = models.CharField(max_length=30)
    actionA3 = models.CharField(max_length=30)
    
    actionB1 = models.CharField(max_length=30)
    actionB2 = models.CharField(max_length=30)
    actionB3 = models.CharField(max_length=30)