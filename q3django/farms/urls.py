from django.urls import path
from . import views

urlpatterns = [
    path('<int:farm_id>', views.show, name='show')
]
