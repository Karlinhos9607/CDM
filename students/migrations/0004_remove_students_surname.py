# Generated by Django 3.0.7 on 2021-02-25 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_subjects_coef'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='surname',
        ),
    ]