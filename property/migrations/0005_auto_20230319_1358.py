# Generated by Django 2.2.24 on 2023-03-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20230319_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(db_index=True, default=False, null=True, verbose_name='Новостройки'),
        ),
    ]