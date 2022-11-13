from django.db import models


class BeerType(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.TextField(null=True)


class Beer(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.TextField(null=True)
    beer_type = models.ForeignKey(BeerType, on_delete=models.DO_NOTHING, null=True)
    photo = models.ImageField(null=True)
