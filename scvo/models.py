from django.db import models


# Create your models here.
class Poliza(models.Model):
    poliza = models.CharField(max_length=20)
    asegurado = models.CharField(max_length=20)
    cuit = models.CharField(max_length=20)
    fecha = models.DateField()

    def __str__(self):
        return self.asegurado + ' ' + self.cuit + ' ' + self.poliza + ' ' + str(self.fecha)
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    cuil = models.CharField(max_length=20)
    id_poliza = models.ForeignKey(Poliza, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nombre + ' ' + self.cuil