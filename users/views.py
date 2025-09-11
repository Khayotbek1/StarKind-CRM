from .serializers import *

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import *
from rest_framework.parsers import FormParser, MultiPartParser

class RegisterAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class AccountDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RegisterSerializer

    def get_object(self):
        return self.request.user


class AdminOrManagerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminOrManager, IsAuthenticated]
    serializer_class = AdminOrManagerRetrieveSerializer
    parser_classes = [MultiPartParser, FormParser]


