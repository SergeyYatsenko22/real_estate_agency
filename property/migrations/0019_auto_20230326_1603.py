# Generated by Django 2.2.24 on 2023-03-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20230326_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(db_index=True, related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
