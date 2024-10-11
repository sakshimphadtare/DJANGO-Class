# Generated by Django 5.1 on 2024-09-12 14:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_app', '0002_alter_teacher_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]