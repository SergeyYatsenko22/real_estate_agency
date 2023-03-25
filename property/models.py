from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name="Имя покемона")
    image = models.ImageField(upload_to="pokemon_images", blank=True,
                              verbose_name="Изображение покемона")
    title_eng = models.CharField(max_length=200, blank=True,
                                 verbose_name="Имя покемона по-английски")
    title_jp = models.CharField(max_length=200, blank=True,
                                verbose_name="Имя покемона по-японски")
    description = models.TextField(blank=True,
                                   verbose_name="Описание покемона")
    previous_evolution = models.ForeignKey("self", null=True, blank=True,
                                           related_name='next_evolutions',
                                           verbose_name="Прошлая эволюция",
                                           on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name="Имя покемона",
                                related_name="entities")
    lat = models.FloatField(null=True, verbose_name="Широта")
    lon = models.FloatField(null=True, verbose_name="Долгота")
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name="Время появления покемона")
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name="Время изчезновения покемона")
    level = models.IntegerField(null=True, blank=True, verbose_name="Уровень покемона")
    health = models.IntegerField(null=True, blank=True, verbose_name="Здоровье покемона")
    strength = models.IntegerField(null=True, blank=True, verbose_name="Сила покемона")
    defence = models.IntegerField(null=True, blank=True, verbose_name="Защита покемона")
    stamina = models.IntegerField(null=True, blank=True, verbose_name="Выносливость покемона")

    def __str__(self):
        return self.pokemon.title

    class Meta:
        verbose_name = "Pokemon entity"
        verbose_name_plural = "Pokemon entities"
