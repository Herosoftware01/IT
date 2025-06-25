from django.contrib import admin
from .models import Empstaff

class EmpstaffAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'admin_image_preview','mobileno', 'wunit', 'workunit', 'hostel',)
    search_fields = ('name', 'wunit', 'workunit')

    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')
        return super().get_queryset(request).using('demo')

admin.site.register(Empstaff, EmpstaffAdmin)

# Register your models here.
