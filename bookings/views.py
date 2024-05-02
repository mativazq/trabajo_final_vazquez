from django.shortcuts import render, redirect


from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Sala, Reserva


# Create your views here.

def home_view(request):
    return render(request, 'bookings/home.html')


# ----------------------------------------------------------------------------------------
# CRUD: SALA
# ----------------------------------------------------------------------------------------

#List

class SalaListView(ListView):
    model = Sala
    template_name = "bookings/vbc/sala_list.html"
    context_object_name = "ADRIANDARGELOS"


class SalaDetailView(DetailView):
    model = Sala
    template_name = "bookings/vbc/sala_detail.html"
    context_object_name = "GUSTAVOCERATI"


class SalaDeleteView(DeleteView):
    model = Sala
    template_name = "bookings/vbc/sala_confirm_delete.html"
    success_url = reverse_lazy("sala-list")


class SalaUpdateView(UpdateView):
    model = Sala
    template_name = "bookings/vbc/sala_form.html"
    fields = ["nombre", "disponible", "capacidad"]
    context_object_name = "sala"
    success_url = reverse_lazy("sala-list")


class SalaCreateView(CreateView):
    model = Sala
    template_name = "bookings/vbc/sala_form.html"
    fields = ["nombre","tipo", "disponible", "capacidad"]
    success_url = reverse_lazy("sala-list")
