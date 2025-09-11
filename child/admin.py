from django.contrib import admin
<<<<<<< HEAD
from .models import *
=======
from django.contrib.auth.models import Group

from .models import Child

admin.site.unregister(Group)
>>>>>>> muzaffar

admin.site.register(Child)
