from django.urls import path
from .models import *
from .views import *


urlpatterns = [
    path('create-list', ChildListCreateAPIView.as_view()),
]