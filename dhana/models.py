from django.db import models

# Create your models here.

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
        db_table = 'Ord_Sample Status'
        app_label = 'dhana'
