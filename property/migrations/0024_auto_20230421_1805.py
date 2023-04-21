# Generated by Django 2.2.24 on 2023-04-21 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0023_auto_20230421_1801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='complaint_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
    ]
