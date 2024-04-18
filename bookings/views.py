from django.shortcuts import render
from django.http import HttpResponse

from .models import Reserva

# Create your views here.

def home_view(request):
    return render(request, "bookings/home.html")