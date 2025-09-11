from django.db import models
<<<<<<< HEAD
from groups.models import Group

class Child(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    parent_name = models.CharField(max_length=255)
    parent_phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    unenrollment_date = models.DateField(auto_now=True,null=True, blank=True)

    def __str__(self):
        return self.full_name
=======
from group.models import Group


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

>>>>>>> muzaffar
