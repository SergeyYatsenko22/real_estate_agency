# Generated by Django 2.2.24 on 2023-04-02 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0020_auto_20230326_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]