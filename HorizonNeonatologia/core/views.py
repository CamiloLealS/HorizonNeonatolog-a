from django.shortcuts import render
from .models import Matrona_Clinica
from .models import Matrona_Coordinadora

# Create your views here.

def home(request):
    return render(request, 'core/home.html')