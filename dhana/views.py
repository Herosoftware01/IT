from django.shortcuts import render
from .models import VueYarnStock,PrintRgbAlt
import pandas as pd
import shutil
import json
import os
from django.conf import settings
from django.http import JsonResponse
from django.db import connections
from rest_framework import viewsets
from .models import PrintRgbAlt,OrdOrderOms
from .serializers import PrintRgbAltSerializer,OrdOrderOmsSerializer
from django.http import StreamingHttpResponse

import time


def orders(request):
    return render(request, 'order_data.html')

class PrintRgbAltViewSet(viewsets.ReadOnlyModelViewSet):  # Only GET API
    queryset = PrintRgbAlt.objects.using('mssql').all()
    serializer_class = PrintRgbAltSerializer

def stream_order_data(request):
    def row_generator():
        conn = connections['mssql']
        cursor = conn.cursor()

        start_total = time.time()
        start_conn = time.time()

        cursor.execute("""
            SELECT *
            FROM HeroPowerBi.dbo.ord_order_oms a WITH (NOLOCK)
            INNER JOIN HeroPowerBi.dbo.[Ord_UDF Complete K] b WITH (NOLOCK)
                ON a.Jobno_Oms = b.[Jobno UDF Complete]
        """)
        connect_time = time.time() - start_conn
        print(f"⏱ SQL Execution Time : {connect_time:.3f} sec")

        # header
        columns = [col[0] for col in cursor.description]
        yield json.dumps(columns) + "\n"

        # fetch in chunks
        fetch_start = time.time()
        while True:
            rows = cursor.fetchmany(100)
            if not rows:
                break
            for row in rows:
                yield json.dumps(row) + "\n"
        fetch_time = time.time() - fetch_start

        total_time = time.time() - start_total
        print(f"✅ Total Time         : {total_time:.3f} sec")
        print(f"⏱ Fetch Time         : {fetch_time:.3f} sec")

    return StreamingHttpResponse(
        row_generator(),
        content_type="application/json"
    )




def get_order_data(request):
    with connections['mssql'].cursor() as cursor:
        query = """
        SELECT * 
        FROM HeroPowerBi.dbo.ord_order_oms a
        INNER JOIN HeroPowerBi.dbo.[Ord_UDF Complete K] b 
            ON a.Jobno_Oms = b.[Jobno UDF Complete]
        """
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

        data = []

        for row in rows:
            record = dict(zip(columns, row))

            if 'mainimagepath' in record and record['mainimagepath']:
                try:
                    raw_path = record['mainimagepath']
                    filename = os.path.basename(raw_path)

                    target_path = os.path.join(settings.MEDIA_ROOT, filename)

                    if not os.path.exists(target_path) and os.path.exists(raw_path):
                        shutil.copyfile(raw_path, target_path)

                    
                    record['mainimageurl'] = f"http://10.1.21.13:7002/media/{filename}"
                except Exception as e:
                    record['mainimageurl'] = ''
                    print(f"Image copy error: {e}")
            else:
                record['mainimageurl'] = ''

            data.append(record)

    return JsonResponse(data, safe=False)





from rest_framework.views import APIView
from rest_framework.response import Response


class OrderWithUdfAPIView(APIView):
    def get(self, request):
        orders = OrdOrderOms.objects.using('mssql').select_related('udf_info').all()
        serializer = OrdOrderOmsSerializer(orders, many=True)
        return Response(serializer.data)


def order_data_api(request):
    data = []

    orders = OrdOrderOms.objects.using('mssql').select_related('udf_info').all()

    for order in orders:
        main_image = order.mainimagepath
        if main_image:
            filename = os.path.basename(main_image)
            main_image = f"http://103.125.155.133:7002/images/{filename}"
        else:
            main_image = None
        row = {
            'jobnoomsnew': order.jobnoomsnew,
            'jobno_oms': order.jobno_oms,
            'insdatenew': order.insdatenew,
            'finaldelvdate1':order.finaldelvdate1,
            'final_year_delivery1':order.final_year_delivery1,
            'pono': order.pono,
            'image_order': order.image_order,
            'printing': order.printing,
            'mainimagepath':main_image,
            # Related (UDF) table fields
            'udf_jobno': order.udf_info.jobno_udf_complete if order.udf_info else None,
            'udf_001_printing': order.udf_info.number_001_printing if order.udf_info else None,
            'udf_002_delivery': order.udf_info.number_002_delivery if order.udf_info else None,
            'udf_046_delivery': order.udf_info.number_046_organic if order.udf_info else None,
            'udf_050_delivery': order.udf_info.number_050_merch if order.udf_info else None,
        }
        data.append(row)

    return JsonResponse(data, safe=False)



def order_delivery(request):
    with connections['mssql'].cursor() as cursor:
        query = """
        SELECT 
            FORMAT(a.finaldelvdate, 'yyyy-MM-dd') AS Finalyeardel,
            FORMAT(a.finaldelvdate, 'dd-MM-yyyy') AS Finaldel,
            a.MainImagePath,
            a.OrderNo,
            g.*
        FROM dbo.txorderdetstyles a
        INNER JOIN txOrdDetStylzUDFs b ON a.OrderNo = b.OrderNo
        INNER JOIN udf_complete g ON a.OrderNo = g.OrderNo_Udf
        WHERE 
            a.ShipmentCompleted = 0 
            AND b.ItemID = 51 
            AND value = 'R';
        """
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

        data = []

        for row in rows:
            record = dict(zip(columns, row))

            main_image = record.get("MainImagePath", "")
            if main_image:
                filename = os.path.basename(main_image)
                record["MainImagePath"] = f"http://103.125.155.133:7002/images/{filename}"
            else:
                record["MainImagePath"] = None  # or '' if you prefer empty string

            data.append(record)
    return JsonResponse(data, safe=False)