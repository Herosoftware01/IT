from django.db import models
from django.utils.html import mark_safe

class OrdStk(models.Model):
    trstype = models.CharField(db_column='Trstype', max_length=6)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=50)  # Field name made lowercase.
    jobno = models.CharField(db_column='Jobno', max_length=50,primary_key=True)  # Field name made lowercase.
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
    
    def admin_image(self):
        if self.orderimage:
            return mark_safe(f'<img src="{self.orderimage}" alt="" width="100" style="border: 1px solid #100; border-radius:10%;"/>')
        return "No Image"
    admin_image.short_description = "OrdImage"

    
    def admin_image1(self):
        if self.tbimage:
            return mark_safe(f'<img src="{self.tbimage}" alt="" width="100" style="border: 1px solid #100; border-radius:10%;"/>')
        return "No Image"
    admin_image1.short_description = "tbImage"




class EmpAttendanceFact(models.Model):

    code_emb_attendance_fact = models.IntegerField(db_column='Code Emb Attendance Fact', blank=True,primary_key= True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    name = models.CharField(max_length=100, blank=True, null=True)

    intime = models.DateTimeField(blank=True, null=True)

    outtime = models.DateTimeField(blank=True, null=True)

    emppic = models.CharField(db_column='Emppic', max_length=8000, blank=True, null=True)  # Field name made lowercase.

    con_code_name_in_out = models.CharField(db_column='Con_Code_name_in_out', max_length=4000, blank=True, null=True)  # Field name made lowercase.

    rel_code_name = models.CharField(db_column='Rel_code_name', max_length=112, blank=True, null=True)  # Field name made lowercase.
  



    class Meta:

        managed = False

        db_table = 'Emp_Attendance_Fact'

    def admin_image_preview(self):
        if self.emppic:
            return mark_safe(f'<img src="{self.emppic}" alt="" width="100" style="border: 1px solid #100; border-radius:10%;"/>')
        return "No Image"
    admin_image_preview.short_description = "Image"

    

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

    jobno = models.CharField(db_column='Jobno', max_length=50,primary_key=True)  # Field name made lowercase.

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

        db_table = 'Ord_Sample_status'
    
    def admin_image_preview(self):
        if self.image:
            return mark_safe(f'<img src="{self.image}" alt="" width="100" style="border: 1px solid #100; border-radius:10%;"/>')
        return "No Image"
    admin_image_preview.short_description = "Image"

    def admin_image_preview1(self):
        if self.topbottomimg:
            return mark_safe(f'<img src="{self.topbottomimg}" alt="" width="100" style="border: 1px solid #100; border-radius:10%;"/>')
        return "No Image"
    admin_image_preview1.short_description = "TbImage"
