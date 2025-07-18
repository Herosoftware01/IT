# Generated by Django 5.0.14 on 2025-07-04 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employeelogin',
            fields=[
                ('code', models.IntegerField(db_column='Code', primary_key=True, serialize=False)),
                ('name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Name', max_length=50)),
                ('hod', models.BooleanField(db_column='HOD')),
                ('hodid', models.IntegerField(blank=True, db_column='HODID', null=True)),
                ('password', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Password', max_length=50, null=True)),
                ('email', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Email', max_length=100, null=True, unique=True)),
                ('ot', models.BooleanField(db_column='OT')),
            ],
            options={
                'db_table': 'EmployeeLogin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empstaff',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobileno', models.CharField(blank=True, max_length=50, null=True)),
                ('wunit', models.CharField(blank=True, max_length=70, null=True)),
                ('workunit', models.CharField(blank=True, db_column='Workunit', max_length=50, null=True)),
                ('hostel', models.CharField(blank=True, max_length=50, null=True)),
                ('emppic', models.CharField(blank=True, db_column='EmpPic', max_length=8000, null=True)),
            ],
            options={
                'db_table': 'EmpStaff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FabYarn',
            fields=[
                ('rate_weight', models.DecimalField(db_column='Rate_Weight', decimal_places=4, max_digits=19)),
                ('img_fpath', models.CharField(blank=True, db_column='Img_Fpath', max_length=8000, null=True)),
                ('fabimg_pen', models.CharField(blank=True, db_column='Fabimg_pen', max_length=67, null=True)),
                ('fabty', models.CharField(db_column='Fabty', max_length=35)),
                ('supplier', models.CharField(max_length=35)),
                ('orderno', models.CharField(max_length=50)),
                ('clr', models.CharField(max_length=50)),
                ('fabric', models.CharField(max_length=35)),
                ('prs', models.CharField(max_length=35)),
                ('kg', models.IntegerField(blank=True, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ty', models.IntegerField()),
                ('hex', models.CharField(max_length=15)),
                ('kw', models.CharField(max_length=1)),
                ('dia', models.CharField(blank=True, max_length=35, null=True)),
                ('image_order', models.CharField(blank=True, db_column='Image Order', max_length=4000, null=True)),
                ('finaldia', models.CharField(blank=True, db_column='FinalDia', max_length=70, null=True)),
            ],
            options={
                'db_table': 'Fab_Yarn',
                'managed': False,
            },
        ),
    ]
