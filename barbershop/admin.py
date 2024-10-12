from django.contrib import admin
from barbershop.models import Barber


class barberAdmin(admin.ModelAdmin):
    list_display = ("username",)
    search_fields = ("__all__",)


admin.site.register(Barber, barberAdmin)
