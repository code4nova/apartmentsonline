from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class ApartmentOwner(models.Model):
    name = models.CharField(max_length=100)
    default_contact = models.CharField(validators=[phone_regex], blank=True,max_length=16)
    def __str__(self):
        return self.name

class ApartmentManager(models.Model):
    name = models.CharField(max_length=100)
    default_contact = models.CharField(validators=[phone_regex], blank=True,max_length=16)
    def __str__(self):
        return self.name

class Apartment(models.Model):
    quality_choices = (
        ("Great", "Great"),
        ("Fair", "Fair"),
        ("Poor", "Poor"),
    )
    phone_contact = models.CharField(validators=[phone_regex], blank=True,max_length=16)
    property_name = models.CharField(max_length=50)
    owned_by = models.ForeignKey(ApartmentOwner)
    managed_by = models.ForeignKey(ApartmentManager)
    number_of_bedrooms = models.PositiveIntegerField()
    property_name = models.CharField(max_length=50)
    max_occupants = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    lease_term = models.PositiveIntegerField()
    maximum_income = models.PositiveIntegerField()
    minimum_income = models.PositiveIntegerField()
    income_divisor = models.PositiveIntegerField()
    rent = models.PositiveIntegerField()
    bus_transit = models.CharField(max_length=20,choices = quality_choices)
    rail_transit = models.CharField(max_length=20,choices = quality_choices)
    def __str__(self):
        return self.property_name
