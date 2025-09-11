from datetime import date

from rest_framework import serializers

from .models import *

class GroupSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(required=False,default=date.today)
    end_date = serializers.DateField(required=False,default=date.today)
    class Meta:
        model = Group
        fields = ['name','branch', 'caregiver', 'start_date', 'end_date']

    def to_internal_value(self, data):
        # Agar frontend bo'sh string yuborsa uni date.today() ga o'zgartirish
        if 'start_date' in data and data['start_date'] == "":
            data['start_date'] = date.today()
        if 'end_date' in data and data['end_date'] == "":
            data['end_date'] = date.today()
        return super().to_internal_value(data)




