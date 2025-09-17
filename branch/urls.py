from django.urls import path
from .views import *

urlpatterns = [
    path('create/', BranchListCreateAPIView.as_view(), name='branch-create-list'),
    path('crud/<int:pk>/',BranchRetrieveUpdateDestroyAPIView.as_view(), name='branch-retrieve-update'),
]