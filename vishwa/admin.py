from django.contrib import admin
from .models import OrdOrderOms

class OrdOrderOmsAdmin(admin.ModelAdmin):
    list_display = ('admin_image_preview','jobno_oms','quantity','buyer','merch','production_unit')
    
    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')

admin.site.register(OrdOrderOms,OrdOrderOmsAdmin)