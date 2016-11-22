from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# TODO: Make this better. Deal with it in JavaScript for now
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

# Base permissions unit, all permissions currently derive from complex
class ApartmentComplex(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "apartment complexes"

# A point of contact for a particular complex
class ApartmentContact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(validators=[phone_regex], blank=True,max_length=16)
    apartment_complex = models.ForeignKey(ApartmentComplex)
    class Meta:
        unique_together = (("phone","apartment_complex"))
    def __str__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.phone)

# Attachment for user model, it's basically just a pro
class ApartmentComplexUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apartment_complex = models.ForeignKey(ApartmentComplex)
    def __str__(self):
        return "%s %s (%s)" % (self.user.first_name,self.user.last_name, self.apartment_complex)

class ApartmentBuilding(models.Model):
    name = models.CharField(max_length=75)
    street_address = models.CharField(max_length=200, unique=True)
    apartment_complex = models.ForeignKey(ApartmentComplex)
    single_unit = models.BooleanField()
    class Meta:
        unique_together = (("name","apartment_complex"))
    def __str__(self):
        return "%s (%s)" % (self.name, self.street_address)

class Apartment(models.Model):
    quality_choices = (
        ("Great", "Great"),
        ("Fair", "Fair"),
        ("Poor", "Poor"),
    )
    building = models.ForeignKey(ApartmentBuilding)
    contact = models.ForeignKey(ApartmentContact)
    number_of_bedrooms = models.PositiveIntegerField()
    suite_number = models.PositiveIntegerField(unique=True)
    max_occupants = models.PositiveIntegerField()
    lease_term = models.PositiveIntegerField()
    maximum_income = models.PositiveIntegerField()
    minimum_income = models.PositiveIntegerField()
    rent = models.PositiveIntegerField()
    bus_transit = models.CharField(max_length=20,choices = quality_choices)
    rail_transit = models.CharField(max_length=20,choices = quality_choices)
    class Meta:
        unique_together = (("building","suite_number"))
    def __str__(self):
        return "Unit %s - %s" % (self.suite_number, self.building.name)
