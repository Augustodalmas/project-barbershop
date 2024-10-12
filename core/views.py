from django.views.generic import CreateView, ListView, DetailView
from core.models import Barbershop


class listBarbershop(ListView):
    model = Barbershop
    template_name = "listBarbershop.html"
    context_object_name = 'barbershops'
    paginate_by = 8

    def get_queryset(self):
        barbershops = super().get_queryset().order_by('name')
        search = self.request.GET.get('search')
        if search:
            barbershops = Barbershop.objects.filter(name__icontains=search)
        return barbershops


class detailBarbershop(DetailView):
    model = Barbershop
    template_name = "detailBarbershop.html"
    context_object_name = "barbershops"
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = self.object.service.all()
        return context
