from django.db import models
from django.utils.html import mark_safe
from django.utils.html import mark_safe
import os
from django.utils.safestring import mark_safe
import shutil
from django.conf import settings

class AllotOrderKisbal(models.Model):
    orderno = models.CharField(db_column='OrderNo', max_length=50, primary_key=True)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=50)  # Field name made lowercase.
    sizes = models.CharField(db_column='Sizes', max_length=35, blank=True, null=True)  # Field name made lowercase.
    totalquantity = models.IntegerField(db_column='TotalQuantity', blank=True, null=True)  # Field name made lowercase.
    jobnoomsnew = models.CharField(db_column='JobnoOmsnew', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orderimage = models.CharField(db_column='OrderImage', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    part = models.CharField(db_column='Part', max_length=50)  # Field name made lowercase.
    tbimage = models.CharField(db_column='TBImage', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    oms_supplier = models.CharField(db_column='OMS_Supplier', max_length=35, blank=True, null=True)  # Field name made lowercase.
    alloted_unit = models.CharField(db_column='Alloted_Unit', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    allotqty = models.IntegerField(blank=True, null=True)
    buyer = models.CharField(db_column='Buyer', max_length=40, blank=True, null=True)  # Field name made lowercase.
    merch = models.CharField(db_column='Merch', max_length=35, blank=True, null=True)  # Field name made lowercase.
    omscol = models.CharField(max_length=50)
    omstb = models.CharField(max_length=50)
    alttb = models.CharField(max_length=70, blank=True, null=True)
    altclr = models.CharField(max_length=70, blank=True, null=True)
    u46 = models.CharField(max_length=750)
    u45141 = models.CharField(max_length=1, blank=True, null=True)
    u50 = models.CharField(max_length=750, blank=True, null=True)
    date = models.CharField(db_column='Date', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='Podate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    dateyear = models.CharField(db_column='Dateyear', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    podateyear = models.CharField(max_length=4000, blank=True, null=True)
    con = models.CharField(db_column='Con', max_length=191, blank=True, null=True)  # Field name made lowercase.
    con_stk = models.CharField(db_column='Con_Stk', max_length=293, blank=True, null=True)  # Field name made lowercase.
    finalyeardelivery = models.CharField(db_column='FinalYearDelivery', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    finaldeldate = models.CharField(db_column='Finaldeldate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    actdate = models.CharField(db_column='Actdate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    actyeardate = models.CharField(db_column='Actyeardate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    con_actdate = models.CharField(db_column='Con_Actdate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    buyer_sh = models.CharField(db_column='Buyer_sh', max_length=6, blank=True, null=True)  # Field name made lowercase.
    punit_sh = models.CharField(db_column='Punit_sh', max_length=6, blank=True, null=True)  # Field name made lowercase.
    director_sample_order = models.CharField(db_column='Director_Sample_Order', max_length=6)  # Field name made lowercase.
    production_type_inside_outside = models.CharField(db_column='Production_type_Inside_Outside', max_length=7, blank=True, null=True)  # Field name made lowercase.
    z_o_yy_findt_dir_sty_uom_pty = models.CharField(db_column='Z_O_yy_Findt_dir_sty_uom_pty', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    allot_con_yy_findt_ordno_mer_punit_aqty = models.CharField(db_column='Allot_Con_yy_Findt_Ordno_mer_PUnit_aqty', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    con_ord_col_tb_f = models.CharField(db_column='Con_Ord_col_tb_f', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    con_ord_col_siz = models.CharField(db_column='Con_Ord_col_siz', max_length=139, blank=True, null=True)  # Field name made lowercase.
    con_ord_col_siz_unit = models.CharField(db_column='Con_Ord_col_siz_Unit', max_length=147, blank=True, null=True)  # Field name made lowercase.
    con_part_clr = models.CharField(db_column='Con_Part_clr', max_length=102, blank=True, null=True)  # Field name made lowercase.
    con_part_clr_altunit_altqty_fdel = models.CharField(db_column='Con_Part_clr_altunit_altqty_fdel', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    con_ord_unit = models.CharField(db_column='Con_ord_unit', max_length=58, blank=True, null=True)  # Field name made lowercase.
    con_tot = models.CharField(db_column='Con_tot', max_length=213, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Allot_Order_KisBal'
        app_label = 'dhana'



class OrdSampleStatus(models.Model):
    print = models.CharField(db_column='Print', max_length=750)  # Field name made lowercase.
    emb = models.CharField(db_column='Emb', max_length=750)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    topbottomimg = models.CharField(db_column='TopBottomImg', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=150)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock')  # Field name made lowercase.
    cutqty = models.IntegerField(db_column='CutQty')  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=10, blank=True, null=True)  # Field name made lowercase.
    o_finaldelvdate = models.DateField(db_column='o_FinalDelvdate', blank=True, null=True)  # Field name made lowercase.
    jobno = models.CharField(db_column='Jobno', max_length=50, primary_key=True)  # Field name made lowercase.
    merch = models.CharField(db_column='Merch', max_length=35, blank=True, null=True)  # Field name made lowercase.
    buy = models.CharField(db_column='Buy', max_length=5, blank=True, null=True)  # Field name made lowercase.
    buyer = models.CharField(db_column='Buyer', max_length=40, blank=True, null=True)  # Field name made lowercase.
    sample_status = models.CharField(db_column='Sample Status', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unitname = models.CharField(db_column='Unitname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    topbottom_des = models.CharField(db_column='TopBottom_des', max_length=50, blank=True, null=True)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sampletype = models.CharField(db_column='Sampletype', max_length=50, blank=True, null=True)  # Field name made lowercase.
    send_dt = models.DateTimeField(db_column='SEND_DT', blank=True, null=True)  # Field name made lowercase.
    apr_dt = models.DateTimeField(db_column='APR_DT', blank=True, null=True)  # Field name made lowercase.
    rej_dt = models.DateTimeField(db_column='REJ_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ord_Sample_Status'
        app_label = 'dhana'



class PrintRgbAlt(models.Model):
    jobno_joint = models.CharField(db_column='Jobno Joint', max_length=50, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prnclr = models.CharField(max_length=50, blank=True, null=True)
    jobno_print_emb = models.CharField(db_column='Jobno Print Emb', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    img_fpath = models.CharField(db_column='Img_Fpath', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    hex = models.CharField(max_length=15, blank=True, null=True)
    prnfile1 = models.CharField(max_length=250, blank=True, null=True)
    prnfile2 = models.CharField(max_length=250, blank=True, null=True)
    imgtb1 = models.CharField(max_length=1550, blank=True, null=True)
    print_img_pen = models.CharField(db_column='Print_img_pen', max_length=13)  # Field name made lowercase.
    image_tb = models.CharField(db_column='Image_tb', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    con_fimg_grclr = models.CharField(db_column='Con_Fimg_grclr', max_length=20, blank=True, null=True)  # Field name made lowercase.
    con_jobno_print = models.CharField(db_column='Con_jobno_Print', max_length=802, blank=True, null=True)  # Field name made lowercase.
    jobno_print_new_rgb = models.CharField(db_column='Jobno_Print_New_RGB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    con_jobno_prndes = models.CharField(db_column='Con_Jobno_PrnDes', max_length=102, blank=True, null=True)  # Field name made lowercase.
    con_jobno_top_clr_line = models.CharField(db_column='Con_jobno_top_clr_line', max_length=200, blank=True, null=True)  # Field name made lowercase.
    con_jobno_top_clr_siz_line = models.CharField(max_length=250, blank=True, null=True)
    con_inout_outsup = models.CharField(db_column='Con_InOut_Outsup', max_length=67, blank=True, null=True)  # Field name made lowercase.
    print_screen_1 = models.CharField(db_column='Print Screen 1', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_screen_2 = models.CharField(db_column='Print Screen 2', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_screen_3 = models.CharField(db_column='Print Screen 3', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    top_bottom = models.CharField(db_column='Top Bottom', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    clrcomb = models.CharField(max_length=100, blank=True, null=True)
    screen_number = models.IntegerField(db_column='Screen Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_type = models.CharField(db_column='Print Type', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_description = models.CharField(db_column='Print Description', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    individual_part_print_emb = models.CharField(db_column='Individual Part Print Emb', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colours = models.IntegerField(db_column='Print Colours', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_emb_ground_colour = models.CharField(db_column='Print & Emb Ground Colour', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inside_outside_print_emb = models.CharField(db_column='Inside,Outside Print Emb', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_emb_outside_supplier = models.CharField(db_column='Print Emb Outside Supplier', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_1 = models.CharField(db_column='Print Colour 1', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_2 = models.CharField(db_column='Print Colour 2', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_3 = models.CharField(db_column='Print Colour 3', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_4 = models.CharField(db_column='Print Colour 4', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_5 = models.CharField(db_column='Print Colour 5', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_6 = models.CharField(db_column='Print Colour 6', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_7 = models.CharField(db_column='Print Colour 7', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_8 = models.CharField(db_column='Print Colour 8', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_size_details = models.CharField(db_column='Print Size Details', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_emb_ground_colour_rgb = models.CharField(db_column='Print & Emb Ground Colour RGB', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    img_print = models.CharField(db_column='Img_Print', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    img_print_mmt = models.CharField(db_column='Img_Print_MMT', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    con_jobno_top_clr_siz = models.CharField(db_column='Con_jobno_top_clr_siz', max_length=256, blank=True, null=True)  # Field name made lowercase.
    con_jobno_top_clr = models.CharField(db_column='Con_jobno_top_clr', max_length=204, blank=True, null=True)  # Field name made lowercase.
    rgb = models.CharField(db_column='RGB', max_length=15, blank=True, null=True)  # Field name made lowercase.
    print_colour_rgb_1 = models.CharField(db_column='Print Colour RGB 1', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_2 = models.CharField(db_column='Print Colour RGB 2', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_3 = models.CharField(db_column='Print Colour RGB 3', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_4 = models.CharField(db_column='Print Colour RGB 4', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_5 = models.CharField(db_column='Print Colour RGB 5', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_6 = models.CharField(db_column='Print Colour RGB 6', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_7 = models.CharField(db_column='Print Colour RGB 7', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_8 = models.CharField(db_column='Print  Colour RGB 8', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    
    def display_order_image(self):
        if self.imgtb1:
            filename = os.path.basename(self.imgtb1)
            dest_path = os.path.join(settings.MEDIA_ROOT, filename)
            # Ensure media folder exists
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
            # Copy only if not already present
            if not os.path.exists(dest_path):
                try:
                    if os.path.exists(self.imgtb1):
                        shutil.copy(self.imgtb1, dest_path)
                    else:
                        return f"❌ Not Found: {self.imgtb1}"
                except Exception as e:
                    return f"❌ Copy failed: {str(e)}"

            return mark_safe(f'<img src="/media/{filename}" width="100" style="border:1px solid #ccc; border-radius:8px;" />')
        return "No Image"
    display_order_image.short_description = "Image TB"

    def img_print_display(self):
        if self.prnfile1:
            filename = os.path.basename(self.prnfile1)
            dest_path = os.path.join(settings.MEDIA_ROOT, filename)
            # Ensure media folder exists
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
            # Copy only if not already present
            if not os.path.exists(dest_path):
                try:
                    if os.path.exists(self.prnfile1):
                        shutil.copy(self.prnfile1, dest_path)
                    else:
                        return f"❌ Not Found: {self.prnfile1}"
                except Exception as e:
                    return f"❌ Copy failed: {str(e)}"

            return mark_safe(f'<img src="/media/{filename}" width="100" style="border:1px solid #ccc; border-radius:8px;" />')
        return "No Image"
    img_print_display.short_description = "Img Print"

    def img_print_mmt_display(self):
        if self.prnfile2:
            filename = os.path.basename(self.prnfile2)
            dest_path = os.path.join(settings.MEDIA_ROOT, filename)
            # Ensure media folder exists
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
            # Copy only if not already present
            if not os.path.exists(dest_path):
                try:
                    if os.path.exists(self.prnfile2):
                        shutil.copy(self.prnfile2, dest_path)
                    else:
                        return f"❌ Not Found: {self.prnfile2}"
                except Exception as e:
                    return f"❌ Copy failed: {str(e)}"

            return mark_safe(f'<img src="/media/{filename}" width="100" style="border:1px solid #ccc; border-radius:8px;" />')
        return "No Image"
    img_print_mmt_display.short_description = "Img Print MMT"

    def get_imgtb1_url(self):
        return self._copy_and_get_url(self.imgtb1)

    def get_prnfile1_url(self):
        return self._copy_and_get_url(self.prnfile1)

    def get_prnfile2_url(self):
        return self._copy_and_get_url(self.prnfile2)

    def _copy_and_get_url(self, full_path):
        if not full_path:
            return None
        filename = os.path.basename(full_path)
        dest_path = os.path.join(settings.MEDIA_ROOT, filename)

        try:
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
            if not os.path.exists(dest_path) and os.path.exists(full_path):
                shutil.copy(full_path, dest_path)
        except Exception as e:
            return f"Error: {str(e)}"
        
        return f"{settings.MEDIA_URL}{filename}"

    class Meta:
        managed = False
        db_table = 'Print_RGB_Alt'
        app_label = 'dhana'

class ImagePrint(models.Model):
    jobno_image_print = models.CharField(db_column='Jobno Image Print', max_length=50,primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ty = models.CharField(max_length=5)
    mainpart = models.CharField(db_column='MainPart', max_length=50)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=50, blank=True, null=True)  # Field name made lowercase.
    indpart = models.CharField(db_column='Indpart', max_length=250)  # Field name made lowercase.
    img_print = models.CharField(db_column='Img_Print', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    img_print_measurement = models.CharField(db_column='Img_Print_measurement', max_length=8000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Image Print'

class VueYarnStock(models.Model):
    date = models.DateTimeField()
    supplierid = models.IntegerField(primary_key=True)
    suppliername = models.CharField(max_length=35, blank=True, null=True)
    orderno = models.CharField(max_length=50, blank=True, null=True)
    yarnid = models.IntegerField(blank=True, null=True)
    yarnname = models.CharField(max_length=35)
    colourid = models.IntegerField(blank=True, null=True)
    clrname = models.CharField(max_length=50)
    kg = models.DecimalField(max_digits=38, decimal_places=10, blank=True, null=True)
    rate = models.DecimalField(max_digits=38, decimal_places=19)

    class Meta:
        managed = False
        db_table = 'vue_Yarn_Stock'

class VueKnitdtlProgramBalance(models.Model):
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    supplier = models.CharField(db_column='Supplier', max_length=35, blank=True, null=True)  # Field name made lowercase.
    no = models.IntegerField(db_column='No')  # Field name made lowercase.
    supplierid = models.IntegerField(db_column='SupplierID')  # Field name made lowercase.
    orderno = models.CharField(db_column='OrderNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fabricid = models.IntegerField(db_column='FabricID',primary_key=True)  # Field name made lowercase.
    colourid = models.IntegerField(db_column='ColourID', blank=True, null=True)  # Field name made lowercase.
    diaid = models.IntegerField(db_column='DiaID')  # Field name made lowercase.
    wgt = models.DecimalField(max_digits=18, decimal_places=4)
    qty = models.DecimalField(db_column='Qty', max_digits=18, decimal_places=4)  # Field name made lowercase.
    rec = models.DecimalField(max_digits=38, decimal_places=4, blank=True, null=True)
    recd1 = models.DecimalField(max_digits=38, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vue_knitdtl_Program_Balance'


class GeneralDeliveryReport(models.Model):
    lz_no = models.IntegerField(db_column='LZ_No',primary_key=True)  # Field name made lowercase.
    le_date = models.DateTimeField(db_column='LE_Date')  # Field name made lowercase.
    lz_reference = models.CharField(db_column='LZ_Reference', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lz_delivery_to = models.CharField(db_column='LZ_Delivery To', max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lz_name = models.CharField(db_column='LZ_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lz_party_ref_no = models.CharField(db_column='LZ_Party Ref No', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lz_vehicle_no = models.CharField(db_column='LZ_Vehicle No', max_length=16, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lz_incharge = models.CharField(db_column='LZ_Incharge', max_length=35, blank=True, null=True)  # Field name made lowercase.
    rf_tot_qty = models.DecimalField(db_column='RF_Tot Qty', max_digits=18, decimal_places=4)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lz_department = models.CharField(db_column='LZ_Department', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lz_completed = models.SmallIntegerField(db_column='LZ_Completed', blank=True, null=True)  # Field name made lowercase.
    sl = models.IntegerField(db_column='Sl', blank=True, null=True)  # Field name made lowercase.
    inwdate = models.DateField(db_column='InwDate', blank=True, null=True)  # Field name made lowercase.
    inwdcno = models.CharField(db_column='InwDcNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qtyreceived = models.IntegerField(db_column='QtyReceived', blank=True, null=True)  # Field name made lowercase.
    ourdcno = models.CharField(db_column='OurDcNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    party = models.CharField(db_column='Party', max_length=50, blank=True, null=True)  # Field name made lowercase.
    verified = models.CharField(db_column='Verified', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inw_date = models.CharField(db_column='Inw_Date', max_length=4000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'General_Delivery_Report'


class EmpMasAll(models.Model):
    code_emb_staff_emp_details = models.IntegerField(db_column='Code Emb Staff Emp Details',primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    dept = models.CharField(max_length=70, blank=True, null=True)
    emppic = models.CharField(db_column='EmpPic', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    rel_code_name_dept = models.CharField(db_column='Rel_code_name_dept', max_length=162, blank=True, null=True)  # Field name made lowercase.
    photo_pending = models.CharField(db_column='Photo Pending', max_length=400, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    con_name_dept_cate_mob_cur_unit = models.CharField(db_column='Con_name_Dept_Cate_mob_Cur_unit', max_length=308, blank=True, null=True)  # Field name made lowercase.
    con_code_hos_m_f_qua_join = models.CharField(db_column='Con_Code_hos_m_f_Qua_join', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    con_acc_acc1_bank = models.CharField(db_column='Con_acc_acc1_bank', max_length=604, blank=True, null=True)  # Field name made lowercase.
    trn = models.CharField(max_length=1, blank=True, null=True)
    sl = models.IntegerField(blank=True, null=True)
    sc = models.CharField(max_length=2, blank=True, null=True)
    code_emb_staff = models.IntegerField(db_column='Code Emb staff', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    category = models.CharField(db_column='Category', max_length=70, blank=True, null=True)  # Field name made lowercase.
    intercom = models.CharField(max_length=50, blank=True, null=True)
    hostel = models.CharField(db_column='Hostel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    roomdtls = models.CharField(db_column='Roomdtls', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orissa = models.CharField(max_length=3, blank=True, null=True)
    bank = models.CharField(db_column='Bank', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accountdetails = models.CharField(db_column='Accountdetails', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grp2 = models.IntegerField(blank=True, null=True)
    prs = models.CharField(max_length=50, blank=True, null=True)
    qualification = models.CharField(db_column='Qualification', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pftype = models.CharField(max_length=10, blank=True, null=True)
    accountdetails1 = models.CharField(db_column='Accountdetails1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    attach = models.CharField(max_length=1550, blank=True, null=True)
    contract_des = models.CharField(max_length=50, blank=True, null=True)
    inch = models.CharField(max_length=3, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    nattgrp = models.CharField(max_length=20, blank=True, null=True)
    salary = models.DecimalField(db_column='Salary', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inspection = models.CharField(db_column='INSPECTION', max_length=3, blank=True, null=True)  # Field name made lowercase.
    empprs = models.CharField(db_column='Empprs', max_length=80, blank=True, null=True)  # Field name made lowercase.
    skilled = models.CharField(max_length=10, blank=True, null=True)
    aempwatch = models.CharField(max_length=3, blank=True, null=True)
    joindt = models.CharField(db_column='Joindt', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    con_ori_roomdtls_skilled_inter_dtls_aemp_watch = models.CharField(db_column='Con_ori_roomdtls_skilled_inter_dtls_aemp_watch', max_length=124, blank=True, null=True)  # Field name made lowercase.
    tasstaff = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Emp_Mas_All'


class Staffpre(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.IntegerField()
    name = models.CharField(max_length=70)
    wunit = models.CharField(max_length=70, blank=True, null=True)
    cat = models.CharField(max_length=70, blank=True, null=True)
    prsdtls = models.CharField(max_length=500, blank=True, null=True)
    prsdis = models.CharField(max_length=500, blank=True, null=True)
    mobileno = models.CharField(max_length=50, blank=True, null=True)
    intercom = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    attach = models.CharField(max_length=1550, blank=True, null=True)
    hostel = models.CharField(max_length=50, blank=True, null=True)
    roomdtls = models.CharField(db_column='Roomdtls', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orissa = models.CharField(max_length=3, blank=True, null=True)
    bank = models.CharField(db_column='Bank', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accountdetails = models.CharField(db_column='Accountdetails', max_length=200, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(max_length=200, blank=True, null=True)
    badd = models.CharField(max_length=200, blank=True, null=True)
    ifscno = models.CharField(max_length=200, blank=True, null=True)
    bact = models.CharField(max_length=1, blank=True, null=True)
    bank1 = models.CharField(max_length=200, blank=True, null=True)
    accountdetails1 = models.CharField(db_column='Accountdetails1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    branch1 = models.CharField(max_length=200, blank=True, null=True)
    badd1 = models.CharField(max_length=200, blank=True, null=True)
    ifscno1 = models.CharField(max_length=200, blank=True, null=True)
    qulification = models.CharField(max_length=50, blank=True, null=True)
    dtjoin = models.DateTimeField(blank=True, null=True)
    dtresign = models.DateTimeField(blank=True, null=True)
    dtrsysdt = models.DateTimeField(blank=True, null=True)
    pftype = models.CharField(max_length=10, blank=True, null=True)
    inch = models.CharField(max_length=3, blank=True, null=True)
    ej = models.DateTimeField(blank=True, null=True)
    vanno = models.CharField(max_length=50, blank=True, null=True)
    pfno = models.CharField(max_length=50, blank=True, null=True)
    esino = models.CharField(max_length=50, blank=True, null=True)
    ladd1 = models.CharField(db_column='LADD1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ladd2 = models.CharField(db_column='LADD2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lcity = models.CharField(max_length=50, blank=True, null=True)
    lstate = models.CharField(max_length=50, blank=True, null=True)
    lpincode = models.CharField(max_length=50, blank=True, null=True)
    padd1 = models.CharField(db_column='PADD1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    padd2 = models.CharField(db_column='PADD2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pcity = models.CharField(db_column='PCITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pstate = models.CharField(db_column='PSTATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ppincode = models.CharField(db_column='PPINCODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emc = models.CharField(db_column='EMC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    relation = models.CharField(max_length=30, blank=True, null=True)
    emc_pers = models.CharField(max_length=50, blank=True, null=True)
    bg = models.CharField(max_length=50, blank=True, null=True)
    time_template = models.CharField(db_column='Time_Template', max_length=20, blank=True, null=True)  # Field name made lowercase.
    esiyn = models.CharField(max_length=3, blank=True, null=True)
    pfyn = models.CharField(max_length=3, blank=True, null=True)
    senior = models.CharField(max_length=3, blank=True, null=True)
    time_template1 = models.CharField(db_column='Time_Template1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField()
    modifieddate = models.DateTimeField()
    timestamp = models.TextField()  # This field type is a guess.
    ebcharge = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    mcategory = models.CharField(db_column='Mcategory', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mcateid = models.IntegerField(db_column='Mcateid', blank=True, null=True)  # Field name made lowercase.
    prab = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'StaffPre'


class TBuyer(models.Model):
    buyerid = models.IntegerField(db_column='BuyerID', primary_key=True)  # Field name made lowercase.
    buyername = models.CharField(db_column='BuyerName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    orderno = models.CharField(db_column='OrderNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    refresh = models.CharField(db_column='Refresh', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_Buyer'
        app_label = 'dhana'



class OrdUdfCompleteK(models.Model):
    jobno_udf_complete = models.CharField(db_column='Jobno UDF Complete', max_length=50, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_001_printing = models.CharField(db_column='001 Printing', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_002_delivery = models.CharField(db_column='002 Delivery', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_003_embroidery = models.CharField(db_column='003 Embroidery', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_004_compacting = models.CharField(db_column='004 Compacting', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_005_cutting = models.CharField(db_column='005 Cutting', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_006_textile = models.CharField(db_column='006 Textile', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_007 = models.CharField(db_column='007', max_length=750, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_008_fabric = models.CharField(db_column='008_Fabric', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_009_carton = models.CharField(db_column='009 Carton', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_010_label = models.CharField(db_column='010 Label', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_011_pr_machine = models.CharField(db_column='011 Pr Machine', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_012_pr_table = models.CharField(db_column='012 Pr Table', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_013_punching = models.CharField(db_column='013 Punching', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_014_dyeing = models.CharField(db_column='014 Dyeing', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_015_transfer = models.CharField(db_column='015 Transfer', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_016_screen = models.CharField(db_column='016 Screen', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_017_doc = models.CharField(db_column='017 Doc', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_018_rib = models.CharField(db_column='018 Rib', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_019_emb_thread = models.CharField(db_column='019 Emb Thread', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_020_yarn = models.CharField(db_column='020 Yarn', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_021_pr_dyes = models.CharField(db_column='021 Pr Dyes', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_022_draw_back = models.CharField(db_column='022 Draw back', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_023_pat_1_size = models.CharField(db_column='023 Pat 1 size', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_024_pat_all_size = models.CharField(db_column='024 Pat all Size', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_025_week = models.CharField(db_column='025 Week', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_026_order_payment = models.CharField(db_column='026 Order payment', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_027_pr_colour_app = models.CharField(db_column='027 Pr Colour App', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_028_pr_flim = models.CharField(db_column='028 Pr Flim', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_029_colour = models.CharField(db_column='029 Colour', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_030_packing_list = models.CharField(db_column='030 Packing List', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_031_inspection = models.CharField(db_column='031 Inspection', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_032_woven = models.CharField(db_column='032 Woven', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_033_carton_slip = models.CharField(db_column='033 CArton Slip', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_034_sample = models.CharField(db_column='034 Sample', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_035 = models.CharField(db_column='035', max_length=750, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_036_fab_in = models.CharField(db_column='036 Fab In', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_037_rotary = models.CharField(db_column='037 Rotary', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_038_extra_fabric = models.CharField(db_column='038 Extra Fabric', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_039_pro_sample = models.CharField(db_column='039 Pro Sample', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_040_lab_test = models.CharField(db_column='040 Lab Test', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_041_ll = models.CharField(db_column='041 LL', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_042_compacting_dia = models.CharField(db_column='042  Compacting Dia', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_043 = models.CharField(db_column='043', max_length=750, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_044 = models.CharField(db_column='044', max_length=750, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_045_stitching = models.CharField(db_column='045 Stitching', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_45_o = models.CharField(db_column='45-O', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_45_r = models.CharField(db_column='45-R', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_45_o_141_o = models.CharField(db_column='45-O/141-O', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_046_organic = models.CharField(db_column='046  Organic', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_047_dyeing_name = models.CharField(db_column='047  Dyeing Name', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_048_com_name = models.CharField(db_column='048   Com Name', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_049_pr_dyes = models.CharField(db_column='049   Pr Dyes', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_050_merch = models.CharField(db_column='050   Merch', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_051_eco = models.CharField(db_column='051   Eco', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_052_sample = models.CharField(db_column='052  Sample', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_053_print_shape_bit = models.CharField(db_column='053  Print Shape Bit', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_054_pr_msmt = models.CharField(db_column='054  Pr Msmt', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_055_emb_details = models.CharField(db_column='055  Emb Details', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_056_print_details = models.CharField(db_column='056  Print Details', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_057_acc_details = models.CharField(db_column='057 Acc Details', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_058_emb_msmt = models.CharField(db_column='058 Emb Msmt', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_059_emb_shape_bit = models.CharField(db_column='059  Emb Shape Bit', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_060_others = models.CharField(db_column='060 Others', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_061_dri = models.CharField(db_column='061 Dri', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_062_amma_godown = models.CharField(db_column='062 Amma Godown', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_063_amma_godown_pro = models.CharField(db_column='063 Amma Godown PRO', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_064_out_side_work = models.CharField(db_column='064 Out Side Work', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_065_label_details = models.CharField(db_column='065 Label Details', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_066_fabric_details = models.CharField(db_column='066 Fabric Details', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_067_t_dia = models.CharField(db_column='067 T Dia', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_068_v_u = models.CharField(db_column='068 V&U', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_069_bc_ac = models.CharField(db_column='069 BC-AC', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_070_pro_qty = models.CharField(db_column='070  Pro Qty', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_071_sup_cmnts = models.CharField(db_column='071 Sup Cmnts', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_072_os_pattern = models.CharField(db_column='072 OS Pattern', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_073_order = models.CharField(db_column='073 Order', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_074_use = models.CharField(db_column='074  use', max_length=750, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_075_e_del_date = models.CharField(db_column='075  E Del Date', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_076_p_del_date = models.CharField(db_column='076  P Del Date', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_077_d_rate = models.CharField(db_column='077 D Rate', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_078_rate = models.CharField(db_column='078 Rate', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_079_lab = models.CharField(db_column='079  Lab', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_080_emb_name = models.CharField(db_column='080 emb name', max_length=750, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_081_d_sample = models.CharField(db_column='081 D Sample', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_082_k_dia_f_dia = models.CharField(db_column='082 K.Dia F.Dia', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_083_c_result = models.CharField(db_column='083 C Result', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_084_doc_description = models.CharField(db_column='084  Doc Description', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_085_a = models.CharField(db_column='085 A', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_086_su_a = models.CharField(db_column='086 Su A', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_089_incharge_name = models.CharField(db_column='089 Incharge Name', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_090 = models.CharField(db_column='090', max_length=750, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_092_copy = models.CharField(db_column='092 copy', max_length=750, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_093_kaja = models.CharField(db_column='093  kaja', max_length=750, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_094_dye_send = models.CharField(db_column='094 dye send', max_length=750, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_095_emb_status = models.CharField(db_column='095 Emb Status', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_096_progaram = models.CharField(db_column='096 PROGARAM', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_097_fab_pro = models.CharField(db_column='097  FAB PRO', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_098_hand_cutting = models.CharField(db_column='098  HAND CUTTING', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_099_contract_cutting = models.CharField(db_column='099  CONTRACT CUTTING', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_101_prg_ch = models.CharField(db_column='101 Prg Ch', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_102_stitch_date = models.CharField(db_column='102 Stitch Date', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_103_emb_date = models.CharField(db_column='103  Emb Date', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_104_print_date = models.CharField(db_column='104  Print Date', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_105_cutting_date = models.CharField(db_column='105  Cutting Date', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_106_merch = models.CharField(db_column='106 MERCH', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_107_viji = models.CharField(db_column='107  VIJI', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_108_mani = models.CharField(db_column='108  MANI', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_109_saba = models.CharField(db_column='109 SABA', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_110_sara = models.CharField(db_column='110 SARA', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_111_mani = models.CharField(db_column='111  MANI', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_112_saba = models.CharField(db_column='112   SABA', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_113_fb = models.CharField(db_column='113  FB', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_114_p = models.CharField(db_column='114 P', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_115_c = models.CharField(db_column='115 C', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_116_final_prog = models.CharField(db_column='116  Final Prog', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_117_cm = models.CharField(db_column='117  CM', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_118_cm_por = models.CharField(db_column='118  CM POR', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_119_dy_st = models.CharField(db_column='119  DY ST', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_120_com_st = models.CharField(db_column='120 COM ST', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_121_cd = models.CharField(db_column='121   CD', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_122_cd_st = models.CharField(db_column='122  CD ST', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_123_yarn = models.CharField(db_column='123 YARN', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_124_ne_drop = models.CharField(db_column='124  NE DROP', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_125_stock_order = models.CharField(db_column='125  STOCK ORDER', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_126_pcs_wt_chk = models.CharField(db_column='126  Pcs WT Chk', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_127_po = models.CharField(db_column='127  po', max_length=750, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_128_box = models.CharField(db_column='128   Box', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_129_sc = models.CharField(db_column='129  SC', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_130_ntgt = models.CharField(db_column='130  NTGT', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_131_priority = models.CharField(db_column='131  PRIORITY', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_132_lf = models.CharField(db_column='132 LF', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_133_lab_po = models.CharField(db_column='133 LAB PO', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_134_lab_dtl = models.CharField(db_column='134  LAB DTL', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_135_roll_check = models.CharField(db_column='135 ROLL CHECK', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_136_fabric_reciever = models.CharField(db_column='136  FABRIC RECIEVER', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_137_pr_emb_msmt = models.CharField(db_column='137  PR EMB MSMT', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_138_yarn = models.CharField(db_column='138  YARN', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_139_cora = models.CharField(db_column='139  CORA', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_140_dyed = models.CharField(db_column='140  DYED', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_141_debit = models.CharField(db_column='141 DEBIT', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_141_r = models.CharField(db_column='141-R', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_141_o = models.CharField(db_column='141-O', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_45141 = models.CharField(db_column='45141', max_length=750, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_142_debit_detail = models.CharField(db_column='142  DEBIT DETAIL', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_143_garment = models.CharField(db_column='143  GARMENT', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_144_garment_detail = models.CharField(db_column='144   GARMENT DETAIL', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_145_label = models.CharField(db_column='145  LABEL', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_146_label_detail = models.CharField(db_column='146  LABEL DETAIL', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_147_textile = models.CharField(db_column='147  TEXTILE', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_148_textile_detail = models.CharField(db_column='148   TEXTILE DETAIL', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_149_a_style = models.CharField(db_column='149  A style', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_150_dd_date = models.CharField(db_column='150 DD DATE', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_151_ready_fab = models.CharField(db_column='151  Ready Fab', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_152_dd_date = models.CharField(db_column='152  DD DATE', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_153_wo = models.CharField(db_column='153   WO', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_154_ex = models.CharField(db_column='154   EX', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_155_press_but = models.CharField(db_column='155   PRESS BUT', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_156_date = models.CharField(db_column='156  DATE', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_157_compacting = models.CharField(db_column='157 COMPACTING', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_158_jakka = models.CharField(db_column='158  JAKKA', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_159_pho_card = models.CharField(db_column='159  PHO CARD', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_160_in_date = models.CharField(db_column='160  IN DATE', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_161_test = models.CharField(db_column='161  TEST', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_162_sup = models.CharField(db_column='162 sup', max_length=750, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_45_r_141_r = models.CharField(db_column='45-R/141-R', max_length=750, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'Ord_UDF Complete K'
        app_label = 'dhana' 



class OrdOrderOms(models.Model):
    udf_info = models.ForeignKey(
        'OrdUdfCompleteK',  # ✅ Use the model name as a string
        to_field='jobno_udf_complete',
        db_column='Jobno_Oms',  # This field exists in this model and points to the UDF table
        on_delete=models.DO_NOTHING,
        related_name='order_records',
        null=True,
        blank=True,
    )
    insdatenew = models.CharField(db_column='insdateNew', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    # jobno_oms = models.CharField(db_column='Jobno_Oms', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    printing = models.CharField(db_column='Printing', max_length=750, blank=True, null=True)  # Field name made lowercase.
    jobnoomsnew = models.CharField(db_column='JobnoOmsnew', max_length=50, primary_key=True)  # Field name made lowercase.
    mainimagepath = models.CharField(max_length=511, blank=True, null=True)
    ordimg1_pen = models.CharField(db_column='OrdImg1_Pen', max_length=9)  # Field name made lowercase.
    styleid = models.IntegerField()
    final_delivery_date = models.CharField(db_column='Final delivery date', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    finaldelvdate1 = models.DateTimeField(blank=True, null=True)
    year = models.CharField(db_column='Year', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    final_year_delivery = models.CharField(db_column='Final Year delivery', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    final_year_delivery1 = models.CharField(db_column='Final Year delivery1', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ddays = models.IntegerField(blank=True, null=True)
    fdays = models.IntegerField(db_column='Fdays', blank=True, null=True)  # Field name made lowercase.
    insdays = models.IntegerField(blank=True, null=True)
    finaldelvdate = models.CharField(db_column='FinalDelvDate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ourdeldate = models.CharField(db_column='Ourdeldate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ourdelvdate = models.CharField(db_column='OurDelvDate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='PODate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    vessel_dt = models.CharField(max_length=4000, blank=True, null=True)
    vessel_yr = models.CharField(max_length=4000, blank=True, null=True)
    pono = models.CharField(db_column='PONo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shipmentcompleted = models.SmallIntegerField(db_column='ShipmentCompleted')  # Field name made lowercase.
    reference = models.CharField(max_length=2100, blank=True, null=True)
    no = models.CharField(db_column='No', max_length=50)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company Name', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mer_un = models.CharField(max_length=71, blank=True, null=True)
    image_order = models.CharField(db_column='Image Order', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    abc = models.CharField(db_column='ABC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    order_follow_up = models.CharField(db_column='Order_Follow_up', max_length=35)  # Field name made lowercase.
    quality_controller = models.CharField(db_column='Quality Controller', max_length=35)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    buyer_sh = models.CharField(db_column='Buyer_sh', max_length=10, blank=True, null=True)  # Field name made lowercase.
    punit_sh = models.CharField(db_column='PUnit_sh', max_length=6, blank=True, null=True)  # Field name made lowercase.
    insdateyear = models.CharField(db_column='insdateYear', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    insdate = models.CharField(db_column='Insdate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    buyer = models.CharField(db_column='Buyer', max_length=15, blank=True, null=True)  # Field name made lowercase.
    merch = models.CharField(max_length=35, blank=True, null=True)
    u46 = models.CharField(max_length=750, blank=True, null=True)
    actdaten = models.DateTimeField(db_column='actdateN', blank=True, null=True)  # Field name made lowercase.
    actdate = models.CharField(db_column='Actdate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    actyeardate = models.CharField(db_column='Actyeardate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    con_actdate = models.CharField(db_column='Con_Actdate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    production_unit = models.CharField(db_column='Production_unit', max_length=35, blank=True, null=True)  # Field name made lowercase.
    director_sample_order = models.CharField(db_column='Director_Sample_Order', max_length=6)  # Field name made lowercase.
    z_o_ordfol_qualitycon = models.CharField(db_column='Z_O_Ordfol_Qualitycon', max_length=72, blank=True, null=True)  # Field name made lowercase.
    con_ordno_mer_buy = models.CharField(db_column='Con_ordno_mer_buy', max_length=95, blank=True, null=True)  # Field name made lowercase.
    con_ord_un_buy_mer_sty_qty = models.CharField(db_column='Con_ord_un_buy_mer_sty_Qty', max_length=173, blank=True, null=True)  # Field name made lowercase.
    z_o_dd_ord_findt_buy_mer_qty = models.CharField(db_column='Z_O_DD_Ord_Findt_Buy_mer_Qty', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    z_o_yy_findt_dir_sty_uom_pty = models.CharField(db_column='Z_O_yy_Findt_dir_sty_uom_pty', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    con_str_sty_uom_prodty = models.CharField(db_column='Con_Str_Sty_UOM_Prodty', max_length=22, blank=True, null=True)  # Field name made lowercase.
    con_findt_ordno_dir_un_buy_uom_qty_mer = models.CharField(db_column='Con_Findt_ordno_dir_un_Buy_Uom_Qty_mer', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    production_type_inside_outside = models.CharField(db_column='Production_type_Inside_Outside', max_length=7, blank=True, null=True)  # Field name made lowercase.
    shipment_complete = models.CharField(db_column='Shipment_complete', max_length=9, blank=True, null=True)  # Field name made lowercase.
    


    @property
    def jobno_oms(self):
        return self.udf_info_id

    def __str__(self):
        return f"{self.udf_info_id} - {self.printing}"
    class Meta:
        managed = False
        db_table = 'Ord_Order_Oms'
        app_label = 'dhana' 



