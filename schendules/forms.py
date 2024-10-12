from schendules.models import Schedule
from django import forms
from django.core.exceptions import ValidationError


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['Responsible', 'date', 'hours', 'client']

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        hours = cleaned_data.get('hours')
        responsible = cleaned_data.get('Responsible')

        # Verifica se já existe um agendamento com os mesmos valores
        if Schedule.objects.filter(date=date, hours=hours, Responsible=responsible).exists():
            raise ValidationError(
                'Já existe um agendamento para essa data, hora e barbeiro.')

        return cleaned_data

    def __init__(self, *args, available_times=None, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        if available_times:
            self.fields['hours'].choices = [
                (hours, hours.strftime('%H:%M')) for hours in available_times]
