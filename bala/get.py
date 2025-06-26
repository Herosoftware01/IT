# This is an auto-generated Django model module.

# You'll have to do the following manually to clean this up:

#   * Rearrange models' order

#   * Make sure each model has one field with primary_key=True

#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior

#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table

# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models





class EmpAttendanceFact(models.Model):

    code_emb_attendance_fact = models.IntegerField(db_column='Code Emb Attendance Fact', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

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

