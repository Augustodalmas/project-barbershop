from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from barbershop.views import createBarber
from core.views import listBarbershop, detailBarbershop
from barbershop.views import createBarber

urlpatterns = [
    path('list/', listBarbershop.as_view(), name='listBarbershops'),
    path('list/<int:pk>/', detailBarbershop.as_view(), name='detailBarbershops'),
    path('list/<int:pk>/register_barber/', createBarber.as_view(), name='createBarber'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
