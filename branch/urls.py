from django.urls import path
from .views import *

urlpatterns = [
    path('create/', BranchCreateAPIView.as_view(), name='branch-create'),
]