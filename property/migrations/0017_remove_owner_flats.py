# Generated by Django 2.2.24 on 2023-03-26 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_flat_owners'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='flats',
        ),
    ]
