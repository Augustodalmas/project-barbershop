from django import forms
from .models import Barber, Service  # Importe o modelo relevante


class BarberForm(forms.ModelForm):
    class Meta:
        model = Barber  # Modelo associado ao formulário
        # Campos a serem incluídos no formulário
        fields = ['username', 'email', 'telephone', 'service']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Definir o queryset dos serviços
        self.fields['service'].queryset = Service.objects.all()
        # Configura o widget como select múltiplo e aplica as classes CSS desejadas
        self.fields['service'].widget.attrs.update({
            'class': 'form-control',
            'multiple': 'multiple'
        })
