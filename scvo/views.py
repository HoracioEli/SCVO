from django.shortcuts import render
from .models import Poliza,Empleado

# Create your views here.
def scvo(request):
    #retornar todos los registros de la tabla poliza ordenados por nombre
    poliza = Poliza.objects.all().order_by('asegurado')
    return render(request, 'scvo.html',{'polizas': poliza})

def bienvenida(request):
    return render(request, 'index.html')