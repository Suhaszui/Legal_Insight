from django.urls import path
from a1.views import home

urlpatterns = [
    path('', home),   # 👈 CHANGE THIS
]