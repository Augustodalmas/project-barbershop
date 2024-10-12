from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import register_view, login_view, logout_view, perfilView
"""createUser, LogoutView,"""
urlpatterns = [
    path('register_user/', register_view, name='createUser'),
    path('login/', login_view, name='loginUser'),
    path('logout/', logout_view, name='logoutUser'),
    path('perfil/<str:user>/<int:pk>/',
         perfilView.as_view(), name='perfil')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)