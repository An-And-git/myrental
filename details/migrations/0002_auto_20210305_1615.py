# Generated by Django 3.1.7 on 2021-03-05 10:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='tenant_ph',
        ),
        migrations.AddField(
            model_name='details',
            name='tenant_phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
