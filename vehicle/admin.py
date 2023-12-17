from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import *


# Register your models here.


class InsuranceModelAdmin(admin.ModelAdmin):
    list_display = ["car", "insurer", "policy_number", "expiry_date"]
    list_filter = ["car", "insurer", "policy_number", "expiry_date"]
    search_fields = ["insurer", "policy_number", "expiry_date"]

    class Meta:
        model = Insurance


admin.site.site_header = "Topline Limited Administration"
admin.site.register(Owner)
admin.site.register(Logbook)
admin.site.register(Cars)
admin.site.register(Insurance, InsuranceModelAdmin)
