from django.contrib import admin

# Register your models here.

# local imports
from company.models import Company, Office


admin.site.register(Office)
admin.site.register(Company)
