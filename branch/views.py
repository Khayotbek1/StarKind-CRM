from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .permissions import *
from .serializers import *

class BranchCreateAPIView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = CreateBranchSerializer
    permission_classes = [IsAdmin,IsAuthenticated]







