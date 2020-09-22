from django.http import HttpResponse
from django.shortcuts import render
from .models import Farm


def index(req):
    fields = Farm.objects.all()
    return render(req, 'index.html', {'fields': fields})
