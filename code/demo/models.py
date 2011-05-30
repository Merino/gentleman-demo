from django.db import models
from gentleman.fields import RichTextField, SourceField

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=20)
    
    address_admin1 = models.CharField(max_length=200)
    address_admin2 = models.CharField(max_length=200)
    address_admin_zipcode = models.CharField(max_length=20)
    address_admin_city  = models.CharField(max_length=200)
    address_admin_country = models.CharField(max_length=250)
    source          = SourceField()
    description     = RichTextField()
    
    field_date  = models.DateField()
    field_time  = models.TimeField()
    field_datetime = models.DateTimeField()
    
    class Meta:
        verbose_name = "klant"
        verbose_name_plural = "klanten"
    
    def __unicode__(self):
        return self.name
    
STATE_CHOICES = (
    ('A', 'Active'),
    ('D', 'Deleted'),
)
    
class Order(models.Model):
    number = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer)
    status  = models.CharField(max_length=20,choices=STATE_CHOICES)
    
    
    
    def __unicode__(self):
        return self.number

class Product(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

class OrderRow(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    
    

    