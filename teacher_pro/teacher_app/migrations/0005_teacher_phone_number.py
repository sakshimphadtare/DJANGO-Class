# Generated by Django 5.1 on 2024-09-12 14:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_app', '0004_remove_teacher_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be exactly 10 digits long.', regex='^\\d{10}$')]),
        ),
    ]
