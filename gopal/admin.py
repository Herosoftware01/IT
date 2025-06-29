from django.contrib import admin
from .models import Empstaff, FabYarn, Employeelogin

class EmpstaffAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'admin_image_preview','mobileno', 'wunit', 'workunit', 'hostel',)
    search_fields = ('name', 'wunit', 'workunit')
    list_filter = ('wunit', 'workunit', 'hostel')
    
    class Media:
        js = ('admin/js/cell-select.js',)
        css = {
            'all': ('admin/css/cell-select.css',)
        }

    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')
        return super().get_queryset(request).using('demo')

class FabYarnAdmin(admin.ModelAdmin):
    list_display = ( 'admin_image_preview','fabty', 'supplier', 'orderno', 'clr', 'fabric', 'prs', 'kg')
    search_fields = ('fabty', 'supplier', 'orderno', 'clr', 'fabric')
    list_filter = ('fabty', 'supplier')
    list_per_page = 10 

    class Media:
        js = ('admin/js/cell-select.js',)
        css = {
            'all': ('admin/css/cell-select.css',)
        }


    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')
        return super().get_queryset(request).using('demo')  

class EmployeeloginAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'hod', 'hodid', 'email')
    search_fields = ('name', 'email')
    list_filter = ('hod',)

    class Media:
        js = ('admin/js/cell-select.js',)
        css = {
            'all': ('admin/css/cell-select.css',)
        }

    def get_queryset(self, request):
        return super().get_queryset(request).using('demo')  

admin.site.register(Empstaff, EmpstaffAdmin)
admin.site.register(FabYarn, FabYarnAdmin)
admin.site.register(Employeelogin, EmployeeloginAdmin)


# Register your models here.
