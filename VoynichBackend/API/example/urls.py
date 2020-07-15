from API.example.views import TestTask
from django.urls import path

urlpatterns = [
    path('test_task/', TestTask.as_view(), name='test_task')
]
