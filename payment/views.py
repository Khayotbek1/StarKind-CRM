from rest_framework import generics, permissions
from .models import  Payment
from .serializers import PaymentSerializer

class PaymentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all().select_related("child", "recorded_by")
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(recorded_by=self.request.user)


class PaymentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all().select_related("child", "recorded_by")
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]



