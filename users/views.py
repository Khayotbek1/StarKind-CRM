from .models import *
from .serializers import *

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import *

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

# wuyrn9c328yrn38yr29
# 3r8cn398ry 32987y


