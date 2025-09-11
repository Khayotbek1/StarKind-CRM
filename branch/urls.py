from django.urls import path
from .views import *

urlpatterns = [
    path('create/', BranchCreateAPIView.as_view(), name='branch-create'),
    path('crud/<int:pk>/',BranchRetrieveUpdateDestroyAPIView.as_view(), name='branch-retrieve-update'),
]