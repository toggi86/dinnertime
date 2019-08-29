from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)


class Recipe(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    description = models.CharField(null=True, blank=True, max_length=200)


class Ingredients(models.Model):
    name = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True)


class Dinner(models.Model):
    REGULAR = 1
    CASUAL = 2
    LESS_REGULAR = 3
    FINEDINE = 4
    SIDEDISH = 5
    type_choices = [
        (REGULAR, 'Regular'),
        (CASUAL, 'Casual'),
        (LESS_REGULAR, 'Less regular'),
        (FINEDINE, 'Fine dine'),
        (SIDEDISH, 'Sidedish'),
    ]

    name = models.CharField(null=True, blank=True, max_length=200)
    descr = models.CharField(null=True, blank=True, max_length=200)
    recipe = models.ForeignKey(Recipe, null=True, on_delete=models.SET_NULL, blank=True)
    link = models.URLField(blank=True, null=True)
    dinner_type = models.IntegerField(choices=type_choices)
