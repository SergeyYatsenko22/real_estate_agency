from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    new_building = models.BooleanField('Новостройки', db_index=True, null=True)

    likes = models.ManyToManyField(User, related_name="liked_flats", blank=True, verbose_name="Кто лайкнул")

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="complaints", verbose_name="Кто жаловался")
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name="complaints",
                             verbose_name="Квартира на которую жаловались")
    text = models.TextField('Текст жалобы', blank=True)

    def __str__(self):
        return self.complaint_text


class Owner(models.Model):
    name = models.CharField('ФИО владельца', db_index=True, max_length=200)
    phonenumber = models.CharField('Номер владельца', db_index=True, max_length=20)
    pure_phone = PhoneNumberField("Нормализованный номер телефона", db_index=True, null=True, blank=True,
                                  region="RU")
    flats = models.ManyToManyField("Flat", related_name="owners", db_index=True,
                                   verbose_name="Квартиры в собственности", )

    def __str__(self):
        return self.owner_name
