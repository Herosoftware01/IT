from django.contrib import admin

from .models import OrdStk
# Register your models here.
class OrdStkAdmin(admin.ModelAdmin):
    list_display = ('trstype', 'total', 'unit', 'jobno', 'tb', 'clr', 'bc', 'sew', 'che', 'irn', 'pack', 'oth', 'mist',
                    'trstype_all', 'deldt', 'merch', 'ip', 'orderimage', 'tbimage',
                    'director_sample_order', 'finaldelvdate', 'final_year_delivery',
                    'insdatenew', 'c')
    search_fields = ('jobno','unit', 'tb', 'clr', 'merch')
    list_filter = ('trstype', 'unit', 'tb', 'clr', 'merch') 

    def get_queryset(self, request):
       return super().get_queryset(request).using('mssql')

admin.site.register(OrdStk,OrdStkAdmin)