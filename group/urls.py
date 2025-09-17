from django.urls import path
from .views import *

urlpatterns = [
        path('create-list/',GroupListCreateAPIView.as_view()),
    path('crud/<int:pk>/', GroupRetrieveUpdateDestroyAPIView.as_view()),
]