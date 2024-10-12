from django.contrib import admin
from schendules.models import Schedule


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("client",)
    search_fields = ("__all__",)


admin.site.register(Schedule, ScheduleAdmin)
