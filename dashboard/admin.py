from django.contrib import admin
from .models import CountryData

class DashboardAdmin(admin.ModelAdmin):
    list_display = ('country', 'population')

# Register your models here.
admin.site.register(CountryData, DashboardAdmin)