from django.db import models
from branch.models import Branch
from users.models import User

class Group(models.Model):
    name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    caregiver = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.caregiver.first_name} - {self.caregiver.last_name})"




