# Generated by Django 2.2.24 on 2023-03-19 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_remove_flat_new_building'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(db_index=True, null=True, verbose_name='Новостройки'),
        ),
    ]
