from django.db import models
from gentleman.fields import *

# Create your models here.
class DefaultField(models.Model):
   auto = models.AutoField(primary_key=True)
   
   biginteger = models.BigIntegerField()
   boolean = models.BooleanField()
   
   char = models.CharField(max_length=30)
   commasepratedinteger = models.CommaSeparatedIntegerField(max_length=30)

   date = models.DateField()
   datetime = models.DateTimeField()
   decimal = models.DecimalField(decimal_places=2, max_digits=5)
   
   email = models.EmailField()
   
   fileupload = models.FileField(upload_to='tmp')
   filepath = models.FilePathField()
   float = models.FloatField()

   # this file needs the PIL lib 
   #image = models.ImageField()
   integer = models.IntegerField()
   ipaddress = models.IPAddressField()
   
   nullboolean = models.NullBooleanField()
   
   positiveinteger = models.PositiveIntegerField()
   positivesmallinteger = models.PositiveSmallIntegerField()

   textarea = models.TextField()
   time = models.TimeField()
   
   url = models.URLField()

class CustomField(models.Model):
    
    normal = models.TextField()
    code = SourceField()
    text = RichTextField()
 
class Boss(models.Model):
    name = models.CharField(max_length=100)
    
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    emailfield = models.CharField(max_length=100)
    boss = models.ForeignKey(Boss)
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    emailfield = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher)
    

class Studie(models.Model):
    name = models.CharField(max_length=200)
    
    
    
    pass
    # Foreignkey
        # select
        # raw_id
        
    # ManyToMany 
        # Horizontal
        # Verticule
        
        
    # Inlines ?