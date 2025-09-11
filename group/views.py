from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .permissions import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from branch.models import Branch

from users.models import User


class GroupListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOrManagerOrCaregiver]  # Admin va Manager yaratishi mumkin

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Group.objects.none()  # Anonymous foydalanuvchi uchun bo‘sh queryset

        if user.is_staff or user.is_superuser:
            return Group.objects.all()

        if user.position == "manager":
            try:
                branch = Branch.objects.get(manager=user)
            except Branch.DoesNotExist:
                return Group.objects.none()
            return Group.objects.filter(branch=branch)

        if user.position == "caregiver":
            return Group.objects.filter(caregiver=user)

        return Group.objects.none()  # Boshqa pozitsiyalar uchun bo‘sh queryset

    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied("❌ Avval tizimga kiring.")

        if user.is_staff or user.is_superuser:
            serializer.save()
            return

        if user.position == "manager":
            try:
                user_branch = Branch.objects.get(manager=user)
            except Branch.DoesNotExist:
                raise PermissionDenied("❌ Sizga branch biriktirilmagan.")

            branch = serializer.validated_data.get("branch")
            if branch != user_branch:
                raise PermissionDenied("❌ Siz faqat o‘z filialingizda group yarata olasiz.")

            serializer.save()
            return

        # Caregiver yoki boshqa pozitsiyalar yaratolmaydi
        raise PermissionDenied("❌ Siz group yaratish huquqiga ega emassiz.")


class GroupRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOrManagerOrCaregiver]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Group.objects.none()

        # 1. Admin yoki Superuser -> hamma grouplar
        if user.is_staff or user.is_superuser or user.position == "admin":
            return Group.objects.all()

        # 2. Manager -> faqat o'z branchidagi grouplar
        if user.position == "manager":
            return Group.objects.filter(branch__manager=user)

        # 3. Caregiver -> faqat o'ziga biriktirilgan group
        if user.position == "caregiver":
            return Group.objects.filter(caregiver=user)

        return Group.objects.none()

    def check_object_permissions(self, request, obj):
        """
        Caregiver faqat GET qilishi mumkin, tahrirlash/o‘chirish taqiqlanadi.
        """
        super().check_object_permissions(request, obj)

        if request.user.position == "caregiver" and request.method not in permissions.SAFE_METHODS:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Caregiver faqat o‘z guruhini ko‘ra oladi.")
