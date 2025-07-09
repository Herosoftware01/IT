# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.html import mark_safe

class OrdOrderOms(models.Model):
    insdatenew = models.CharField(db_column='insdateNew', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    jobno_oms = models.CharField(db_column='Jobno Oms', max_length=50,primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jobnoomsnew = models.CharField(db_column='JobnoOmsnew', max_length=50, blank=True, null=True)  # Field name made lowercase.
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

    class Meta:
        managed = False
        db_table = 'Ord_Order_Oms'

    def admin_image_preview(self):
        if self.image_order:
            return mark_safe(f'<img src="{self.image_order}" alt="" width="100" style="border: 1px solid #100; border-radius:10%;"/>')
        return "No Image"
    admin_image_preview.short_description = "Image"