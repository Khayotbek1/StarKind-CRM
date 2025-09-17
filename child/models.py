from django.db import models
from group.models import Group
from datetime import date

class Child(models.Model):


    class Status (models.TextChoices):
        ACTIVE = "active", "Active"
        LEFT = "left", "Left"
        GRADUATED = "graduated", "Graduated"

    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    parent_name = models.CharField(max_length=255)
    parent_phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    unenrollment_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    balance = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.name} ({self.group.name})"

    @property
    def total_paid(self):
        """Bolaga qilingan jami to‘lovlar"""
        return sum(p.amount_paid for p in self.payments.all())

    @property
    def total_due(self):
        """Qancha summa to‘lanishi kerak (boshlagan sanadan bugungacha)"""
        today = date.today()
        months = (today.year - self.enrollment_date.year) * 12 + (today.month - self.enrollment_date.month) + 1
        monthly_fee = getattr(self.group, "monthly_fee", 0)
        return months * monthly_fee

    @property
    def debt(self):
        """Qarzdorlik (due - paid)"""
        return self.total_due - self.total_paid


