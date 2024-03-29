# Generated by Django 4.2.5 on 2024-01-04 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Diabetes', '0003_rename_age_diabetes_data_p_age_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diabetes_data',
            old_name='p_age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='diabetes_data',
            old_name='p_blood_Pressure',
            new_name='blood_Pressure',
        ),
        migrations.RenameField(
            model_name='diabetes_data',
            old_name='p_bmi',
            new_name='bmi',
        ),
        migrations.RenameField(
            model_name='diabetes_data',
            old_name='p_gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='diabetes_data',
            old_name='p_glucose',
            new_name='glucose',
        ),
        migrations.RenameField(
            model_name='diabetes_data',
            old_name='p_insulin',
            new_name='insulin',
        ),
        migrations.RenameField(
            model_name='diabetes_data',
            old_name='p_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='diabetes_data',
            old_name='p_pregnancy',
            new_name='pregnancy',
        ),
        migrations.RenameField(
            model_name='diabetes_data',
            old_name='p_time',
            new_name='time',
        ),
    ]
