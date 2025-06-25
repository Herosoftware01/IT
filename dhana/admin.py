from django.contrib import admin
from django.contrib import admin
from django.utils.html import format_html
from .models import AllotOrderKisbal


class AllotOrderKisbalAdmin(admin.ModelAdmin):
    list_display = (
        'display_order_image','orderno', 'colour', 'con_tot', 'sizes',
        'totalquantity', 'jobnoomsnew','part','tbimage','oms_supplier','alloted_unit','quantity','allotqty','buyer','merch','omscol','omstb','alttb','altclr','u46','u45141','u50','date','podate','dateyear','podateyear','con','con_stk','finalyeardelivery','finaldeldate','actdate','actyeardate','con_actdate','buyer_sh','punit_sh','director_sample_order','production_type_inside_outside','z_o_yy_findt_dir_sty_uom_pty','allot_con_yy_findt_ordno_mer_punit_aqty','con_ord_col_tb_f','con_ord_col_siz','con_ord_col_siz_unit','con_part_clr','con_part_clr_altunit_altqty_fdel','con_ord_unit','con_tot'
    )

    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')

    def display_order_image(self, obj):
        if obj.orderimage:
            return format_html('<img src="{}" width="100" height="100" />', obj.orderimage)
        return "-"
    display_order_image.short_description = 'Order Image'

admin.site.register(AllotOrderKisbal, AllotOrderKisbalAdmin)