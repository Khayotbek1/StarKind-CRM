from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .permissions import *
from .serializers import *

class BranchListCreateAPIView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = CreateBranchSerializer
    permission_classes = [IsAdmin]

class BranchRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CreateBranchSerializer
    permission_classes = [IsAdminOrManager]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        user = self.request.user

        if getattr(self, 'swagger_fake_view', False):
            return Branch.objects.none()

        if user.is_staff or user.is_superuser:
            return Branch.objects.all()

        if user.is_authenticated:
            return Branch.objects.filter(manager=user)

        return Branch.objects.none()











