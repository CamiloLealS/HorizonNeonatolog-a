from django.contrib import admin
from .models import Matrona_Clinica
from .models import Matrona_Coordinadora

# Register your models here.

admin.site.register(Matrona_Coordinadora)
admin.site.register(Matrona_Clinica)