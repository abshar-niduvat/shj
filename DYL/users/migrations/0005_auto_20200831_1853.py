# Generated by Django 3.0.7 on 2020-08-31 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200831_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='formes',
            field=models.FileField(upload_to='form/'),
        ),
    ]
