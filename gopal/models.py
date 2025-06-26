# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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
