from django.urls import path
from .views import created_robots

urlpatterns = [
    path('new_robots', created_robots, name='models_robots_view'),
]