# Generated by Django 4.2.5 on 2024-01-04 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Diabetes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diabetes_data',
            old_name='bp',
            new_name='blood_Pressure',
        ),
    ]