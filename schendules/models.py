# models.py
from django.db import models
from barbershop.models import Barber, Barbershop
from accounts.models import Usuario


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    hours = models.TimeField()
    Responsible = models.ForeignKey(
        Barber, on_delete=models.CASCADE, related_name="Schedule_Service")
    barbershop = models.ForeignKey(
        Barbershop, on_delete=models.CASCADE, related_name="schendule_barbershop", null=True, blank=True)


    def __str__(self):
        return f"{self.Responsible}: {self.date} - {self.hours} (Client: {self.client})"
