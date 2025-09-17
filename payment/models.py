from django.db import models
from child.models import Child
from users.models import User

class Payment(models.Model):
    class PaymentStatus(models.TextChoices):
        PAID = "paid", "Paid"
        PARTIALLY_PAID = "partially paid", "Partially Paid"
        UNPAID = "unpaid", "Unpaid"


    child = models.ForeignKey(Child, on_delete=models.SET_NULL, null=True, related_name="payments")
    month = models.DateField(help_text="Qaysi oy uchun to'lov qilindi")
    amount_due = models.DecimalField(max_digits=10, decimal_places=2,help_text="Kompaniya belgilagan summa")
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2,help_text="Mijoz tomonidan to‘langan summa")
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=PaymentStatus.choices, default=PaymentStatus.UNPAID)
    recorded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="payments_recorded")

    def save(self, *args, **kwargs):
        """To'lov statusini avtomatik belgilash"""
        if self.amount_paid >= self.amount_due:
            self.status = self.PaymentStatus.PAID
        elif 0 < self.amount_paid < self.amount_due:
            self.status = self.PaymentStatus.PARTIALLY_PAID
        else:
            self.status = self.PaymentStatus.UNPAID
        super().save(*args, **kwargs)

    def __str__(self):
        recorder = self.recorded_by.username if self.recorded_by else "System"
        return (
            f"{self.child.name if self.child else 'Unknown Child'} | "
            f"{self.month.strftime('%Y-%m')} | "
            f"{self.amount_paid} / {self.amount_due} so'm | "
            f"Status: {self.status} | by {recorder}"
        )


