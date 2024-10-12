# views.py
from django.views.generic import CreateView, ListView
from .models import Schedule, Barber
from barbershop.models import Barbershop
from .forms import ScheduleForm
from datetime import datetime, time
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

BARBER_SHOP_HOURS = [(time(hour, 0), f"{hour}:00") for hour in range(8, 20)]


class ScheduleCreateView(CreateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'create_schedule.html'
    success_url = reverse_lazy('detailBarbershops')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['barbers'] = Barber.objects.all()

        selected_date = self.request.GET.get(
            'date')
        if selected_date:
            selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
            occupied_times = Schedule.objects.filter(
                date=selected_date).values_list('hours', flat=True)
            available_times = [
                hours for hours, _ in BARBER_SHOP_HOURS if hours not in occupied_times]
        else:
            available_times = [hours for hours, _ in BARBER_SHOP_HOURS]
        context['available_times'] = available_times
        context['selected_date'] = selected_date
        return context

    def form_valid(self, form):
        pk = self.kwargs['pk']
        form.instance.client = self.request.user
        barbershop_id = self.kwargs.get('pk')
        barbershop = get_object_or_404(Barbershop, id=barbershop_id)
        form.instance.barbershop = barbershop
        self.success_url = reverse_lazy('detailBarbershops', kwargs={'pk': pk})
        return super().form_valid(form)


class ScheduleListView(ListView):
    model = Schedule
    template_name = 'schedule_list.html'
    context_object_name = 'schedules'
    ordering = ['date', 'hours']
