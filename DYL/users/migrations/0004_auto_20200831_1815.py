# Generated by Django 3.0.7 on 2020-08-31 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_patient_form'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='form',
            new_name='formes',
        ),
    ]
