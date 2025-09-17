from django.contrib import admin
from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from django.db.models import DecimalField

from .models import Child


class DebtFilter(admin.SimpleListFilter):
    title = "Qarzdorlik"
    parameter_name = "debt"

    def lookups(self, request, model_admin):
        return [
            ("bor", "Qarzdorligi bor"),
            ("yoq", "Qarzdorligi yo‘q"),
        ]

    def queryset(self, request, queryset):
        queryset = queryset.annotate(
            annotated_total_paid=Coalesce(
                Sum("payments__amount_paid"),
                Value(0, output_field=DecimalField())
            ),
        )
        required_amount = 1000000  # kontrakt summasi

        if self.value() == "bor":
            return queryset.filter(annotated_total_paid__lt=required_amount)
        elif self.value() == "yoq":
            return queryset.filter(annotated_total_paid__gte=required_amount)
        return queryset



@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ("name", "branch_display", "group", "balance")
    list_filter = (DebtFilter,)

    def branch_display(self, obj):
        return obj.group.branch.name if obj.group and obj.group.branch else "-"
    branch_display.short_description = "Branch"

    def qarzdorlik(self, obj):
        total_paid = obj.payments.aggregate(total=Sum("amount_paid"))["total"] or 0
        required_amount = 1000000
        return max(required_amount - total_paid, 0)
    qarzdorlik.short_description = "Qarzdorligi"
