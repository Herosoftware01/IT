from django.contrib import admin

from .models import OrdStk,EmpAttendanceFact
# Register your models here.
class OrdStkAdmin(admin.ModelAdmin):
    list_display = ('admin_image','admin_image1','trstype', 'total', 'unit', 'jobno', 'tb', 'clr', 'bc', 'sew', 'che', 'irn', 'pack', 'oth', 'mist',
                    'trstype_all', 'deldt', 'merch', 'ip', 'orderimage', 'tbimage',
                    'director_sample_order', 'finaldelvdate', 'final_year_delivery',
                    'insdatenew', 'c')
    search_fields = ('jobno','unit', 'tb', 'clr', 'merch')
    list_filter = ('trstype', 'unit', 'tb', 'clr', 'merch') 
    
  
    def get_queryset(self, request):
       return super().get_queryset(request).using('mssql')

class EmpAttendanceFactAdmin(admin.ModelAdmin):
    list_display = ('admin_image_preview','code_emb_attendance_fact', 'date', 'name', 'intime', 'outtime',
                    'con_code_name_in_out', 'rel_code_name')        
    search_fields = ('name', 'con_code_name_in_out', 'rel_code_name')   
  

    def get_queryset(self, request):
       return super().get_queryset(request).using('mssql')

admin.site.register(OrdStk,OrdStkAdmin)
admin.site.register(EmpAttendanceFact, EmpAttendanceFactAdmin)