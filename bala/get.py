# This is an auto-generated Django model module.

# You'll have to do the following manually to clean this up:

#   * Rearrange models' order

#   * Make sure each model has one field with primary_key=True

#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior

#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table

# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models





class FabRgbMatrplan(models.Model):

    tbimg = models.CharField(max_length=8000, blank=True, null=True)

    jobno = models.CharField(db_column='Jobno', max_length=50)  # Field name made lowercase.

    combocolor = models.CharField(db_column='ComboColor', max_length=50, blank=True, null=True)  # Field name made lowercase.

    mp = models.CharField(max_length=50, blank=True, null=True)

    ip = models.CharField(max_length=50, blank=True, null=True)

    dyeclr = models.CharField(db_column='Dyeclr', max_length=50, blank=True, null=True)  # Field name made lowercase.

    prnclr = models.CharField(db_column='Prnclr', max_length=50, blank=True, null=True)  # Field name made lowercase.

    gsm = models.IntegerField(db_column='GSM')  # Field name made lowercase.

    fdia = models.CharField(db_column='Fdia', max_length=70, blank=True, null=True)  # Field name made lowercase.

    kdia = models.CharField(max_length=35)

    pcswgt = models.CharField(max_length=70, blank=True, null=True)

    size = models.CharField(max_length=35)

    losspercent = models.DecimalField(db_column='LossPercent', max_digits=5, decimal_places=2)  # Field name made lowercase.

    quantity = models.DecimalField(db_column='Quantity', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    fabricno = models.IntegerField(db_column='FabricNo')  # Field name made lowercase.

    ord_image = models.CharField(db_column='Ord_image', max_length=8000, blank=True, null=True)  # Field name made lowercase.

    hex = models.CharField(max_length=15, blank=True, null=True)

    fimage = models.CharField(db_column='Fimage', max_length=8000)  # Field name made lowercase.

    fabty = models.CharField(db_column='FabTy', max_length=35, blank=True, null=True)  # Field name made lowercase.

    withoutfabimg = models.CharField(db_column='WithOutFabImg', max_length=13)  # Field name made lowercase.

    withoutrgb = models.CharField(db_column='WithOutRGB', max_length=10)  # Field name made lowercase.

    fabric = models.CharField(db_column='Fabric', max_length=35)  # Field name made lowercase.

    yarninfo = models.CharField(db_column='YarnInfo', max_length=971, blank=True, null=True)  # Field name made lowercase.

    ll = models.CharField(max_length=114)

    con_dyeclr_prnclr = models.CharField(db_column='Con_dyeclr_prnclr', max_length=102, blank=True, null=True)  # Field name made lowercase.

    con_ord_clr_fab = models.CharField(db_column='Con_Ord_Clr_Fab', max_length=139, blank=True, null=True)  # Field name made lowercase.

    withoutll = models.CharField(max_length=9)

    o_buyer = models.CharField(db_column='O_Buyer', max_length=40, blank=True, null=True)  # Field name made lowercase.

    o_merch = models.CharField(db_column='O_Merch', max_length=35, blank=True, null=True)  # Field name made lowercase.

    o_productionunit = models.CharField(db_column='O_ProductionUnit', max_length=35, blank=True, null=True)  # Field name made lowercase.

    o_ordtype = models.CharField(db_column='O_OrdType', max_length=6)  # Field name made lowercase.

    o_prodtype = models.CharField(db_column='O_ProdType', max_length=7)  # Field name made lowercase.

    con = models.CharField(db_column='Con', max_length=193, blank=True, null=True)  # Field name made lowercase.

    o_styledesc = models.CharField(db_column='o_StyleDesc', max_length=35, blank=True, null=True)  # Field name made lowercase.

    director = models.CharField(max_length=35)

    planned = models.IntegerField(db_column='Planned')  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'Fab_RGB_matrplan'

