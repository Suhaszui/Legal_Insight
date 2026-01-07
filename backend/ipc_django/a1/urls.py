
from django.urls import path,include
from a1.views import home
urlpatterns = [
    path('a1/', home),
]