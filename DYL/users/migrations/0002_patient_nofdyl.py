# Generated by Django 3.0.7 on 2020-08-08 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='nofdyl',
            field=models.CharField(default=10, max_length=100),
            preserve_default=False,
        ),
    ]