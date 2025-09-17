from django.urls import path
from .views import *

urlpatterns = [
    path('list-create/', PaymentListCreateAPIView.as_view(), name='payment-list-create'),
    path("<int:pk>/", PaymentRetrieveUpdateDestroyAPIView.as_view(), name="payment-detail"),
]