from django.db import models
from django.contrib.auth.models import User
from stdimage.models import StdImageField

EASE = (
    (0, 'Très facile'),
    (1, 'Facile'),
    (2, 'Moyenne'),
    (3, 'Difficile'),
)

PRICE = (
    (0, 'Bon marché'),
    (1, 'Moyen'),
    (2, 'Assez cher'),
)

SEX = (
    (0, 'Homme'),
    (1, 'Femme'),
)

ACTIVITY = (
    (0, 'Jamais'),
    (1, 'De temps en temps'),
    (2, 'Souvent'),
    (3, 'Tous le temps'),
)


class Profile(models.Model):
    owner = models.ForeignKey(User)
    is_owner_profile = models.BooleanField(default=False)
    name = models.CharField(max_length=64)
    birthday = models.DateField()
    weight = models.IntegerField()
    height = models.IntegerField()
    sex = models.IntegerField(choices=SEX)
    activity = models.IntegerField(choices=ACTIVITY)
    picture = StdImageField(upload_to='media/images/profile')

    unlikes = models.ManyToManyField('Ingredient')
    unlikes_family = models.ManyToManyField('IngredientFamily')
    diets = models.ManyToManyField('Diet')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=128)
    picture = StdImageField(upload_to='media/images/recipe')
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    amount = models.IntegerField()
    difficulty = models.IntegerField(choices=EASE)
    price = models.IntegerField(choices=PRICE)  # FIXME : exact quantification? -> check marmiton
    steps = models.TextField()
    detail = models.TextField()
    drink = models.TextField()
    origin_url = models.URLField()

    ingredients = models.ManyToManyField('Ingredient')
    #category = models.CharField()  # TODO : relation

    def __str__(self):
        return self.name


class Diet(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    picture = StdImageField(upload_to='media/images/diet')

    ingredients = models.ManyToManyField('Ingredient')
    ingredients_family = models.ManyToManyField('IngredientFamily')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=32)
    picture = StdImageField(upload_to='media/images/ingredient')
    description = models.TextField(default="")
    # country =  #  FIXME : use it for local menu generation
    # season?
    family = models.ForeignKey('IngredientFamily')
    nutriments = models.ManyToManyField('Nutriment', through='IngredientNutriment')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class IngredientNutriment(models.Model):
    ingredient = models.ForeignKey('Ingredient')
    nutriment = models.ForeignKey('Nutriment')
    quantity = models.FloatField()


class IngredientFamily(models.Model):
    name = models.CharField(max_length=32)
    picture = StdImageField(upload_to='media/images/ingredient_family')

    ingredients = models.ManyToManyField('Ingredient')

    # TODO (addition by Kevin) : seems necessary for hierarchy (to discuss)
    father = models.ForeignKey('IngredientFamily', null=True, default=None)

    def __str__(self):
        return self.name


class Nutriment(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=32)
    people_n = models.IntegerField()
    price = models.IntegerField(choices=PRICE)
    difficulty = models.IntegerField(choices=EASE)
    owner = models.ForeignKey(User)
    # FIXME : missing order/planning relationship (will do it soon) - kevin
    recipes = models.ManyToManyField('Recipe')

    def __str__(self):
        return self.name
