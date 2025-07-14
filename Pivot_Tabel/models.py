
from django.db import models
from django.utils.html import mark_safe


class Empstaff(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    mobileno = models.CharField(max_length=50, blank=True, null=True)
    wunit = models.CharField(max_length=70, blank=True, null=True)
    workunit = models.CharField(db_column='Workunit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hostel = models.CharField(max_length=50, blank=True, null=True)
    emppic = models.CharField(db_column='EmpPic', max_length=8000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmpStaff'
    
    def admin_image_preview(self):
        if self.emppic:
            return mark_safe(f'<img src="{self.emppic}" alt="" width="100" style="border: 1px solid #100; border-radius:10%;"/>')
        return "No Image"
    admin_image_preview.short_description = "Image"

class FabYarn(models.Model):
    rate_weight = models.DecimalField(db_column='Rate_Weight', max_digits=19, decimal_places=4)  # Field name made lowercase.
    img_fpath = models.CharField(db_column='Img_Fpath', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    fabimg_pen = models.CharField(db_column='Fabimg_pen', max_length=67, blank=True, null=True)  # Field name made lowercase.
    fabty = models.CharField(db_column='Fabty', max_length=35)  # Field name made lowercase.
    supplier = models.CharField(max_length=35)
    orderno = models.CharField(max_length=50)
    clr = models.CharField(max_length=50)
    fabric = models.CharField(max_length=35)
    prs = models.CharField(max_length=35)
    kg = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    ty = models.IntegerField()
    hex = models.CharField(max_length=15)
    kw = models.CharField(max_length=1)
    dia = models.CharField(max_length=35, blank=True, null=True)
    image_order = models.CharField(db_column='Image Order', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    finaldia = models.CharField(db_column='FinalDia', max_length=70, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fab_Yarn'
    
    def admin_image_preview(self):
        if self.image_order:
            return mark_safe(f'<img src="{self.image_order}" alt="" width="100" style="border: 1px solid #100; border-radius:10%;"/>')
        return "No Image"
    admin_image_preview.short_description = "Image"


class Employeelogin(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    hod = models.BooleanField(db_column='HOD')  # Field name made lowercase.
    hodid = models.IntegerField(db_column='HODID', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ot = models.BooleanField(db_column='OT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmployeeLogin'

class OrdStk(models.Model):
    trstype = models.CharField(db_column='Trstype', max_length=6)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=50)  # Field name made lowercase.
    jobno = models.CharField(db_column='Jobno', max_length=50, primary_key=True)  # Field name made lowercase.
    tb = models.CharField(db_column='Tb', max_length=50)  # Field name made lowercase.
    clr = models.CharField(max_length=50)
    bc = models.IntegerField()
    sew = models.IntegerField()
    che = models.IntegerField()
    irn = models.IntegerField()
    pack = models.IntegerField()
    oth = models.IntegerField()
    mist = models.IntegerField()
    trstype_all = models.CharField(max_length=80, blank=True, null=True)
    deldt = models.DateTimeField(db_column='DelDt')  # Field name made lowercase.
    merch = models.CharField(db_column='MERCH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(max_length=50)
    orderimage = models.CharField(db_column='OrderImage', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    tbimage = models.CharField(db_column='TBImage', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    director_sample_order = models.CharField(db_column='Director_Sample_Order', max_length=6, blank=True, null=True)  # Field name made lowercase.
    finaldelvdate = models.CharField(db_column='FinalDelvDate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    final_year_delivery = models.CharField(db_column='Final Year delivery', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insdatenew = models.CharField(db_column='insdateNew', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    c = models.IntegerField(db_column='C')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ord_stk'
    
    def admin_image_preview(self):
        if self.orderimage:
            return mark_safe(f'<img src="{self.orderimage}" alt="" width="100" style="border: 1px solid #100; border-radius:10%;"/>')
        return "No Image"
    admin_image_preview.short_description = "Image"

    def admin_image_preview_tb(self):
        if self.tbimage:
            return mark_safe(f'<img src="{self.tbimage}" alt="" width="100" style="border: 1px solid #100; border-radius:10%;"/>')
        return "No Image"
    admin_image_preview_tb.short_description = "Image"

