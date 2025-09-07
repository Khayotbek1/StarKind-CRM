from django.db import models
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
