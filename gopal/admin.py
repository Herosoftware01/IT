from django.contrib import admin
from .models import Empstaff, FabYarn, Employeelogin , OrdStk
from pivot import PivotTableMixin


class EmpstaffAdmin(PivotTableMixin,admin.ModelAdmin):
    list_display = ('code', 'name', 'admin_image_preview','mobileno', 'wunit', 'workunit', 'hostel',)
    # search_fields = ('name', 'wunit', 'workunit')
    # list_filter = ('wunit', 'workunit', 'hostel')
    pivot_fields = ('code', 'name', 'admin_image_preview','mobileno', 'wunit', 'workunit', 'hostel',)
    
    class Media:
        js = ('admin/js/cell-select.js',)
        css = {
            'all': ('admin/css/cell-select.css',)
        }

    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')
        return super().get_queryset(request).using('demo')

class FabYarnAdmin(PivotTableMixin,admin.ModelAdmin):
    list_display = ( 'admin_image_preview','fabty', 'supplier', 'orderno', 'clr', 'fabric', 'prs', 'kg')
    # search_fields = ('fabty', 'supplier', 'orderno', 'clr', 'fabric')
    # list_filter = ('fabty', 'supplier')
    # list_per_page = 10 
    pivot_fields = ['image_order','fabty', 'supplier', 'orderno', 'clr', 'fabric', 'prs', 'kg']

    class Media:
        js = ('admin/js/cell-select.js',)
        css = {
            'all': ('admin/css/cell-select.css',)
        }


    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')
        # return super().get_queryset(request).using('demo')  

class EmployeeloginAdmin(PivotTableMixin,admin.ModelAdmin):
    list_display = ('code', 'name', 'hod', 'hodid', 'email')
    # search_fields = ('name', 'email')
    # list_filter = ('hod',)
    pivot_fields = ['code', 'name', 'hod', 'hodid', 'email']

    class Media:
        js = ('admin/js/cell-select.js',)
        css = {
            'all': ('admin/css/cell-select.css',)
        }

    def get_queryset(self, request):
        return super().get_queryset(request).using('demo')  

class OrdStkAdmin(PivotTableMixin,admin.ModelAdmin):
    list_display = ('admin_image_preview','admin_image_preview_tb', 'trstype', 'jobno', 'tb', 'total', 'unit', 'clr', 'bc', 'sew','che','irn', 'pack', 'oth', 'mist', 'trstype_all', 'deldt', 'merch', 'ip','director_sample_order','finaldelvdate','final_year_delivery','insdatenew','c',)
    # search_fields = ('trstype', 'jobno', 'tb')
    # list_filter = ('trstype',)
    pivot_fields = ['orderimage','tbimage','trstype', 'total', 'unit', 'jobno', 'tb', 'clr', 'bc', 'sew','che', 'irn', 'pack', 'oth', 'mist', 'trstype_all', 'deldt', 'merch', 'ip','director_sample_order','finaldelvdate','final_year_delivery','insdatenew','c',]

    class Media:
        js = ('admin/js/cell-select.js',)
        css = {
            'all': ('admin/css/cell-select.css',)
        }

    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')

admin.site.register(Empstaff, EmpstaffAdmin)
admin.site.register(FabYarn, FabYarnAdmin)
admin.site.register(Employeelogin, EmployeeloginAdmin)
admin.site.register(OrdStk, OrdStkAdmin)


# Register your models here.
