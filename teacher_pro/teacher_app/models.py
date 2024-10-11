from django.db import models
from django.core.validators import MaxValueValidator
import re
from django.core.validators import RegexValidator

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Phone number must be exactly 10 digits long.'
            )
        ],
        blank=True,
        null=True,
    )
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Create your models here.
