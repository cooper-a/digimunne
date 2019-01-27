from django.contrib import admin
from .models import Patient
from .models import Vaccination

# Register your models here.
admin.site.register(Vaccination)
admin.site.register(Patient)