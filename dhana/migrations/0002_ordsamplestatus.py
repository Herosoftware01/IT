
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhana', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdSampleStatus',
            fields=[
                ('print', models.CharField(db_column='Print', max_length=750)),
                ('emb', models.CharField(db_column='Emb', max_length=750)),
                ('date', models.DateTimeField(blank=True, db_column='DATE', null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=20, null=True)),
                ('image', models.CharField(blank=True, db_column='Image', max_length=8000, null=True)),
                ('topbottomimg', models.CharField(blank=True, db_column='TopBottomImg', max_length=8000, null=True)),
                ('remarks', models.CharField(db_column='Remarks', max_length=150)),
                ('stock', models.IntegerField(db_column='Stock')),
                ('cutqty', models.IntegerField(db_column='CutQty')),
                ('active', models.CharField(blank=True, db_column='Active', max_length=10, null=True)),
                ('o_finaldelvdate', models.DateField(blank=True, db_column='o_FinalDelvdate', null=True)),
                ('jobno', models.CharField(db_column='Jobno', max_length=50, primary_key=True, serialize=False)),
                ('merch', models.CharField(blank=True, db_column='Merch', max_length=35, null=True)),
                ('buy', models.CharField(blank=True, db_column='Buy', max_length=5, null=True)),
                ('buyer', models.CharField(blank=True, db_column='Buyer', max_length=40, null=True)),
                ('sample_status', models.CharField(blank=True, db_column='Sample Status', max_length=15, null=True)),
                ('unitname', models.CharField(blank=True, db_column='Unitname', max_length=50, null=True)),
                ('topbottom_des', models.CharField(blank=True, db_column='TopBottom_des', max_length=50, null=True)),
                ('colour', models.CharField(blank=True, db_column='Colour', max_length=50, null=True)),
                ('sampletype', models.CharField(blank=True, db_column='Sampletype', max_length=50, null=True)),
                ('send_dt', models.DateTimeField(blank=True, db_column='SEND_DT', null=True)),
                ('apr_dt', models.DateTimeField(blank=True, db_column='APR_DT', null=True)),
                ('rej_dt', models.DateTimeField(blank=True, db_column='REJ_DT', null=True)),
            ],
            options={
                'db_table': 'Ord_Sample Status',
                'managed': False,
            },
        ),
    ]
