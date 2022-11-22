from django.db import models

# Create your models here.

class Matrona(models.Model):
    id_usuario = models.AutoField(primary_key=True, default=100)
    id_superior = models.IntegerField(null=True)
    nombre = models.TextField(max_length=50)
    paterno = models.TextField(max_length=50)
    materno = models.TextField(max_length=50, null=True)

    def __str__(self) -> str:
        return self.nombre + self.paterno

class Matrona_Clinica(Matrona):
    def __str__(self) -> str:
        return super().__str__()

class Matrona_Coordinadora(Matrona):
    def __str__(self) -> str:
        return super().__str__()

