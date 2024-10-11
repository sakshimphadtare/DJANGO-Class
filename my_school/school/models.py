from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE) 
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.name
