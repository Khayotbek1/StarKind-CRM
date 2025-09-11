from rest_framework import generics

from .serializer import *
from .permissions import *

class ChildListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ChildSerializer
    permission_classes = [IsAdminOrManagerOrCaregiver]




