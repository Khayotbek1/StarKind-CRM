from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Child

admin.site.unregister(Group)

admin.site.register(Child)
