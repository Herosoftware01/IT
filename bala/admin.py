from django.contrib import admin

from .models import OrdStk,EmpAttendanceFact,OrdSampleStatus
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
    
class OrdSampleStatusAdmin(admin.ModelAdmin):
    list_display = ('admin_image_preview','admin_image_preview1','jobno','print',  'date', 'status', 'remarks', 'stock',
                    'cutqty', 'active', 'o_finaldelvdate', 'merch', 'buy',
                    'buyer', 'sample_status', 'unitname', 'topbottom_des','emb',
                    'colour', 'sampletype', 'send_dt', 'apr_dt', 'rej_dt')
    search_fields = ('jobno','merch','buyer','sample_status')

    def get_queryset(self, request):
       return super().get_queryset(request).using('mssql')

admin.site.register(OrdStk,OrdStkAdmin)
admin.site.register(EmpAttendanceFact, EmpAttendanceFactAdmin)
admin.site.register(OrdSampleStatus, OrdSampleStatusAdmin)