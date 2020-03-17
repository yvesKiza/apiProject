from django.contrib import admin

# Register your models here.
from . models import hospital

class HospitalAdmin(admin.ModelAdmin):
    list_display=('name','key','number_test')

admin.site.register(hospital,HospitalAdmin)