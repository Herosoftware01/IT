from django.db import models


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