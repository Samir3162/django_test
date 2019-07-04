# django imports
from django.db import models

# Create your models here.


class Company(models.Model):

    name = models.CharField(max_length=300)


class Office(models.Model):

    headquater = models.BooleanField(default=False)
    street = models.CharField(max_length=256, blank=True)
    postal_code = models.CharField(max_length=32, blank=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    company = models.ForeignKey('Company', related_name='company_office') 
    monthly_rent = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
