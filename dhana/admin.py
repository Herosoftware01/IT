from django.contrib import admin
from django.utils.html import format_html
from .models import AllotOrderKisbal,OrdSampleStatus,PrintRgbAlt,ImagePrint,VueYarnStock,VueKnitdtlProgramBalance,GeneralDeliveryReport,EmpMasAll,Staffpre,TBuyer,OrdOrderOms,OrdUdfCompleteK
from django.utils.html import mark_safe
import os
from django.utils.safestring import mark_safe
import shutil
from django.conf import settings


class AllotOrderKisbalAdmin(admin.ModelAdmin):
    list_display = (
        'display_order_image','display_order_image1','orderno', 'colour', 'con_tot', 'sizes','totalquantity', 'jobnoomsnew','part','tbimage','oms_supplier','alloted_unit','quantity','allotqty','buyer','merch','omscol','omstb','alttb','altclr','u46','u45141','u50','date','podate','dateyear','podateyear','con','con_stk','finalyeardelivery','finaldeldate','actdate','actyeardate','con_actdate','buyer_sh','punit_sh','director_sample_order','production_type_inside_outside','z_o_yy_findt_dir_sty_uom_pty','allot_con_yy_findt_ordno_mer_punit_aqty','con_ord_col_tb_f','con_ord_col_siz','con_ord_col_siz_unit','con_part_clr','con_part_clr_altunit_altqty_fdel','con_ord_unit','con_tot'
    )

    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')

    def display_order_image(self, obj):
        if obj.orderimage:
            return format_html('<img src="{}" width="100" height="100" />', obj.orderimage)
        return "-"
    display_order_image.short_description = 'Order Image'

    def display_order_image1(self, obj):
        if obj.tbimage:
            return format_html('<img src="{}" width="100" height="100" />', obj.tbimage)
        return "-"
    display_order_image.short_description = 'TB Image'

    class Media:
        js = ('admin/js/cell-select.js',)
        css = {
            'all': ('admin/css/cell-select.css',)
        }


class OrdSampleStatusAdmin(admin.ModelAdmin):
    list_display = ('print','display_order_image','emb','status','topbottomimg','remarks','stock','cutqty','active','o_finaldelvdate','jobno','merch','buy','buyer','sample_status'
    )

    def get_queryset(self, request):
       return super().get_queryset(request).using('mssql')

    def display_order_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image)
        return "-"
    display_order_image.short_description = 'Order Image'
    class Media:
        js = ('admin/js/cell-select.js',)
        css = {
            'all': ('admin/css/cell-select.css',)
        }


class PrintRgbAltAdmin(admin.ModelAdmin):
    list_display = (
        'display_order_image', 'img_print_display', 'img_print_mmt_display','img_fpath_display', 'jobno_joint', 'prnclr',
        'screen_number', 'jobno_print_emb',  'hex', 'print_img_pen', 'con_fimg_grclr',
        'con_jobno_print', 'jobno_print_new_rgb', 'con_jobno_prndes', 'con_jobno_top_clr_line',
        'con_jobno_top_clr_siz_line', 'con_inout_outsup', 'print_screen_1', 'print_screen_2',
        'print_screen_3', 'top_bottom', 'clrcomb', 'print_type', 'print_description',
        'individual_part_print_emb', 'print_colours', 'print_emb_ground_colour',
        'inside_outside_print_emb', 'print_emb_outside_supplier', 'print_colour_1', 'print_colour_2',
        'print_colour_3', 'print_colour_4', 'print_colour_5', 'print_colour_6', 'print_colour_7',
        'print_colour_8', 'print_size_details', 'print_emb_ground_colour_rgb',
        'con_jobno_top_clr_siz', 'con_jobno_top_clr', 'rgb', 'print_colour_rgb_1',
        'print_colour_rgb_2', 'print_colour_rgb_3', 'print_colour_rgb_4', 'print_colour_rgb_5',
        'print_colour_rgb_6', 'print_colour_rgb_7', 'print_colour_rgb_8'
    )

    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')
    


    # def img_print_mmt_display(self, obj):
    #     if obj.img_print_mmt:
    #         return format_html('<img src="{}" width="100" height="100" />', obj.img_print_mmt)
    #     return "-"
    # img_print_mmt_display.short_description = 'Img Print MMT'

    def img_fpath_display(self, obj):
        if obj.img_fpath:
            return format_html('<img src="{}" width="100" height="100" />', obj.img_fpath)
        return "-"
    img_fpath_display.short_description = 'img fpath display'

    class Media:
        js = ('admin/js/cell-select.js',)
        css = {
            'all': ('admin/css/cell-select.css',)
        }


class ImagePrintAdmin(admin.ModelAdmin):
    list_display = (
        'jobno_image_print','ty','mainpart','color','indpart','display_order_image','img_print_measurement_display'
    )

    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')

    def display_order_image(self, obj):
        if obj.img_print:
            return format_html('<img src="{}" width="100" height="100" />', obj.img_print)
        return "-"
    display_order_image.short_description = 'img print'

    def img_print_measurement_display(self, obj):
        if obj.img_print_measurement:
            return format_html('<img src="{}" width="100" height="100" />', obj.img_print_measurement)
        return "-"
    img_print_measurement_display.short_description = 'img print measurement'

    class Media:
        js = ('admin/js/cell-select.js',)
        css = {
            'all': ('admin/css/cell-select.css',)
        }


class VueYarnStockAdmin(admin.ModelAdmin):
    list_display = (
        'date','supplierid','suppliername','orderno','yarnid','yarnname','colourid','clrname','kg','rate'
    )

    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')
    
class VueKnitdtlProgramBalanceAdmin(admin.ModelAdmin):
    list_display = (
        'date','supplier','no','supplierid','orderno','fabricid','colourid','diaid','wgt','qty','rec','recd1'
    )

    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')
    
    class Media:
        js = ('admin/js/cell-select.js',)
        css = {
            'all': ('admin/css/cell-select.css',)
        }


class GeneralDeliveryReportAdmin(admin.ModelAdmin):
    list_display = (
        'lz_no','le_date','lz_reference','lz_delivery_to','lz_name','lz_party_ref_no','lz_vehicle_no','lz_incharge','rf_tot_qty','lz_department','lz_completed','sl','inwdate','inwdcno','qtyreceived','ourdcno','party','verified','inw_date'
    )

    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')
    
    class Media:
        js = ('admin/js/cell-select.js',)
        css = {
            'all': ('admin/css/cell-select.css',)
        }


# class EmpMasAllAdmin(admin.ModelAdmin):
#     list_display = (
#         'code_emb_staff_emp_details','name','mobile','dept','emppic','rel_code_name_dept','photo_pending','con_name_dept_cate_mob_cur_unit','con_code_hos_m_f_qua_join','con_acc_acc1_bank','trn','sl','sc','code_emb_staff','category','intercom','hostel','roomdtls','orissa','bank','accountdetails','grp2','prs','qualification','pftype','accountdetails1','attach','contract_des','inch','sex','nattgrp','salary','inspection','empprs','skilled','aempwatch','joindt','con_ori_roomdtls_skilled_inter_dtls_aemp_watch','tasstaff'
#     )

#     def get_queryset(self, request):
#         return super().get_queryset(request).using('mssql')


class EmpMasAllAdmin(admin.ModelAdmin):
    list_display = (
        'code_emb_staff_emp_details','name','mobile','dept','emppic','rel_code_name_dept','photo_pending',
        'con_name_dept_cate_mob_cur_unit','con_code_hos_m_f_qua_join','con_acc_acc1_bank','trn','sl','sc',
        'code_emb_staff','category','intercom','hostel','roomdtls','orissa','bank','accountdetails','grp2',
        'prs','qualification','pftype','accountdetails1','attach','contract_des','inch','sex','nattgrp',
        'salary','inspection','empprs','skilled','aempwatch','joindt',
        'con_ori_roomdtls_skilled_inter_dtls_aemp_watch','tasstaff'
    )

    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')
    
    def changelist_view(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}
        extra_context['custom_button'] = True  
        return super().changelist_view(request, extra_context=extra_context)

    def has_add_permission(self, request):
        return True

    class Media:
        js = ('admin/js/cell-select.js',)
        css = {
            'all': ('admin/css/cell-select.css',)
        }


class StaffpreAdmin(admin.ModelAdmin):
    list_display = (
        'code','name','wunit','cat','prsdtls','prsdis','mobileno',
        'intercom','status','attach','hostel','roomdtls','orissa',
        'bank','accountdetails','branch','badd','ifscno','bact','bank1','accountdetails1','branch1',
        'badd1','ifscno1','qulification','dtjoin','dtresign','dtrsysdt','pftype','inch','ej',
        'vanno','pfno','esino','ladd1','ladd2','lcity',
        'lstate','lpincode','padd1','padd2','pcity','pstate','ppincode','emc','relation','emc_pers','bg',
        'time_template','esiyn','pfyn','senior','time_template1','createdate','modifieddate','timestamp',
        'id','ebcharge','mcategory','lastname','mcateid','prab'
    )

    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')

    class Media:
        js = ('admin/js/cell-select.js',)
        css = {
            'all': ('admin/css/cell-select.css',)
        }


# class TBuyerAdmin(admin.ModelAdmin):
#     list_display = ('buyerid', 'buyername', 'orderno', 'date', 'guid', 'refresh')

#     def get_queryset(self, request):
#         return super().get_queryset(request).using('demo')

#     def save_model(self, request, obj, form, change):
#         obj.save(using='demo')


# admin.site.register(TBuyer,TBuyerAdmin)


##

#

class OrdUdfCompleteKAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')
    
class OrdOrderOmsAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).using('mssql')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "udf_info":
            kwargs["queryset"] = OrdUdfCompleteK.objects.using('mssql').all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(OrdUdfCompleteK, OrdUdfCompleteKAdmin)
admin.site.register(OrdOrderOms, OrdOrderOmsAdmin)

admin.site.register(Staffpre, StaffpreAdmin)
admin.site.register(EmpMasAll, EmpMasAllAdmin)
admin.site.register(GeneralDeliveryReport, GeneralDeliveryReportAdmin)
admin.site.register(VueKnitdtlProgramBalance, VueKnitdtlProgramBalanceAdmin)
admin.site.register(VueYarnStock, VueYarnStockAdmin)
admin.site.register(ImagePrint, ImagePrintAdmin)
admin.site.register(PrintRgbAlt, PrintRgbAltAdmin)
admin.site.register(OrdSampleStatus, OrdSampleStatusAdmin)
admin.site.register(AllotOrderKisbal, AllotOrderKisbalAdmin)