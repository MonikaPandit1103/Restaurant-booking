from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.models import User

def validate_unique_dob(value):
    if Customer.objects.filter(dob=value).exists():
        raise ValidationError("DOB must be unique")

class Customer(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    CITY = 'City'
    VILLAGE = 'Village'
    LOCATION_CHOICES = [
        (CITY, 'City'),
        (VILLAGE, 'Village'),
    ]

    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    dob = models.DateField(unique=True, validators=[validate_unique_dob])
    age = models.PositiveIntegerField()
    married = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
    image = models.ImageField(upload_to='customers/', blank=True, null=True)

    def save(self, *args, **kwargs):
        today = date.today()
        self.age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
