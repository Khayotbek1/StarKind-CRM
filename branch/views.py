from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .permissions import *
from .serializers import *

class BranchCreateAPIView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = CreateBranchSerializer
    permission_classes = [IsAdmin]

class BranchRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CreateBranchSerializer
    permission_classes = [IsAdminOrManager]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Branch.objects.all()
        return Branch.objects.filter(manager=user)











