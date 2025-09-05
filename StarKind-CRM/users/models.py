from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    class Position (models.TextChoices):
        ADMIN = "admin", "Adminsitrator"
        MANAGER = "manager", "Manager"
        TEACHER = "teacher", "Teacher"
        CAREGIVER = "caregiver", "Caregiver"
        ACCOUNTANT = "accountant", "Accountant"
        OTHER = "other", "Other"

    class Status (models.TextChoices):
        ACTIVE = "active", "Active"
        LEFT = "left", "Left"
        POSITION_CHANGED = "position_changed", "Position Changed"

    phone = models.CharField(max_length=20, unique=True)
    position = models.CharField(max_length=20, choices=Position.choices, default=Position.OTHER)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    start_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_position_display()})"

