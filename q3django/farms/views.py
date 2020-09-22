from django.http import HttpResponse
from django.shortcuts import render
from .models import Farm, Field


def show(req, farm_id):
    farm = Farm.objects.get(pk=farm_id)
    fields = Field.objects.filter(farm_id=farm_id)
    return render(req, 'show.html', {'farm': farm, 'fields': fields})
