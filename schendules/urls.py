# urls.py
from django.urls import path
from schendules.views import ScheduleCreateView, ScheduleListView

urlpatterns = [
    path('list/<int:pk>/schedule/create/',
         ScheduleCreateView.as_view(), name='create_schedule'),
    path('list/<int:pk>/schedule/',
         ScheduleListView.as_view(), name='schedule_list'),
]
