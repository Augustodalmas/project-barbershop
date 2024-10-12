from barbershop.forms import BarberForm
from barbershop.models import Barber
from core.models import Barbershop
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView
from django.shortcuts import render


class createBarber(CreateView):
    model = Barber
    form_class = BarberForm
    template_name = 'registrobarbeiro.html'
    success_url = "/detailBarbershops/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        modelo_principal = get_object_or_404(
            Barbershop, pk=self.kwargs['pk'])  # Obtenção da FK da barbershop
        # Adicionando a FK ao contecxt
        context['modelo_principal'] = modelo_principal
        return context

    def form_valid(self, form):
        form.instance.is_owner_id = self.request.user
        modelo_principal = get_object_or_404(Barbershop, pk=self.kwargs['pk'])
        # Cria uma instancia que não foi salva no banco ainda
        barber = form.save(commit=False)
        barber.barbershop = modelo_principal
        barber.save()
        return redirect('listBarbershops')
