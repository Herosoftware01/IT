# This is an auto-generated Django model module.

# You'll have to do the following manually to clean this up:

#   * Rearrange models' order

#   * Make sure each model has one field with primary_key=True

#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior

#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table

# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models





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

    jobno = models.CharField(db_column='Jobno', max_length=50)  # Field name made lowercase.

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

