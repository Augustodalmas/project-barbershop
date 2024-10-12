from django.contrib import admin
from core.models import Plan, Subscription, Barbershop, Service

class planAdmin(admin.ModelAdmin):
    list_display = ("name_plan",)
    search_fields = ("__all__",)


class subscriptionAdmin(admin.ModelAdmin):
    list_display = ("subscription_id",)
    search_fields = ("__all__",)


class barbershopAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("__all__",)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("__all__",)


admin.site.register(Plan, planAdmin)
admin.site.register(Subscription, subscriptionAdmin)
admin.site.register(Barbershop, barbershopAdmin)
admin.site.register(Service, ServiceAdmin)

