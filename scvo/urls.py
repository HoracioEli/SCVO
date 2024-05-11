from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name="bienvenida"),
    path('SCVO', views.scvo, name="scvo"),
]