# Generated by Django 2.2.24 on 2023-03-26 11:14

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20230326_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(db_index=True, related_name='flats_by_owner', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, null=True, region='RU', verbose_name='Нормализованный номер телефона'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owners_phonenumber',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца'),
        ),
    ]