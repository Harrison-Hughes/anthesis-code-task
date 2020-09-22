from django.db import models

# Create your models here.


class Farm(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Field(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    size_in_sq_km = models.FloatField()
    produce = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
