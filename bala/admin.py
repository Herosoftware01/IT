from django.contrib import admin

from .models import OrdStk,EmpAttendanceFact,OrdSampleStatus,AllotPen,FabRgbMatrplan
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
    

class AllotPenAdmin(admin.ModelAdmin):
    list_display = ('jobno_oms', 'jobnoomsnew', 'ordimg1_pen', 'final_delivery_date',
                    'finaldelvdate1', 'year', 'final_year_delivery', 'ddays', 'fdays',
                    'insdays', 'finaldelvdate', 'ourdeldate', 'date', 'ourdelvdate',
                    'podate', 'vessel_dt', 'vessel_yr', 'pono', 'shipmentcompleted',
                    'reference', 'no', 'company_name', 'image_order', 'abc',
                    'order_follow_up')

    search_fields = ('jobno_oms','jobnoomsnew','pono','company_name')

    def get_queryset(self, request):
       return super().get_queryset(request).using('mssql') 

class FabRgbMatrplanAdmin(admin.ModelAdmin):           
    list_display = ('jobno', 'combocolor', 'mp', 'ip', 'dyeclr', 'prnclr',
                        'gsm', 'fdia', 'kdia', 'pcswgt', 'size', 'losspercent',
                        'quantity', 'fabricno', 'ord_image', 'hex', 'fimage',
                        'fabty', 'withoutfabimg', 'withoutrgb', 'fabric',
                        'yarninfo', 'll', 'con_dyeclr_prnclr',
                        'con_ord_clr_fab', 'withoutll', 'o_buyer',
                        'o_merch')

    search_fields = ('jobno','combocolor','mp','ip','dyeclr','prnclr')              
    list_filter = ('jobno', 'combocolor', 'mp', 'ip', 'dyeclr', 'prnclr')
            
    def get_queryset(self, request):
       return super().get_queryset(request).using('mssql') 
    
admin.site.register(OrdStk,OrdStkAdmin)
admin.site.register(EmpAttendanceFact, EmpAttendanceFactAdmin)
admin.site.register(OrdSampleStatus, OrdSampleStatusAdmin)
admin.site.register(AllotPen, AllotPenAdmin)
admin.site.register(FabRgbMatrplan, FabRgbMatrplanAdmin)    

