from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    child_name = serializers.CharField(source='child.name', read_only=True)
    recorded_by_username = serializers.CharField(source="recorded_by.username", read_only=True)

    class Meta:
        model = Payment
        fields = "__all__"

        read_only_fields = ["id", "payment_date", "recorded_by"]

    def create(self, validated_data):
        """recorded_by maydonini avtomatik foydalanuvchi bilan to‘ldirish"""
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            validated_data["recorded_by"] = request.user
        return super().create(validated_data)