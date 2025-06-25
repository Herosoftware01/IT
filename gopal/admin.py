from django.contrib import admin
from .models import Empstaff, OrdStk

class EmpstaffAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'admin_image_preview','mobileno', 'wunit', 'workunit', 'hostel',)
    search_fields = ('name', 'wunit', 'workunit')
    list_filter = ('wunit', 'workunit', 'hostel')
   

    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')
        return super().get_queryset(request).using('demo')

class ordStkAdmin(admin.ModelAdmin):
    list_display = ('trstype', 'total', 'unit', 'jobno', 'tb', 'clr', 'bc', 'sew', 'che', 'irn', 'pack', 'oth', 'mist',
                    'trstype_all', 'deldt', 'merch', 'admin_image_preview', 'tbimage',
                    'director_sample_order', 'finaldelvdate', 'final_year_delivery', 'insdatenew', 'c')
    search_fields = ('jobno',)
    list_filter = ('trstype',)

    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')
        return super().get_queryset(request).using('demo')

admin.site.register(Empstaff, EmpstaffAdmin)
admin.site.register(OrdStk, ordStkAdmin)

# Register your models here.
