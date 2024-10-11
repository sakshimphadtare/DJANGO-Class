from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)  # CharField
    last_name = models.CharField(max_length=50)   # CharField
    age = models.IntegerField()                   # IntegerField
    email = models.EmailField(unique=True)        # EmailField
    is_enrolled = models.BooleanField(default=True)  # BooleanField
    enrollment_date = models.DateField()          # DateField
    GPA = models.DecimalField(max_digits=3, decimal_places=2)  # DecimalField

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
