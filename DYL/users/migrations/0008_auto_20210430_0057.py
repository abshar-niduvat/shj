# Generated by Django 3.1.1 on 2021-04-29 19:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200831_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='dateofapp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='dist_approve_by',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]
