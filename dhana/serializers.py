from rest_framework import serializers
from .models import PrintRgbAlt,OrdOrderOms, OrdUdfCompleteK
from urllib.parse import urljoin

class PrintRgbAltSerializer(serializers.ModelSerializer):
    imgtb1_url = serializers.SerializerMethodField()
    prnfile1_url = serializers.SerializerMethodField()
    prnfile2_url = serializers.SerializerMethodField()

    class Meta:
        model = PrintRgbAlt
        fields = [
            'jobno_joint',
            'jobno_print_emb',
            'imgtb1_url',
            'prnfile1_url',
            'prnfile2_url',
        ]

    def get_imgtb1_url(self, obj):
        return self._build_absolute_url(obj.get_imgtb1_url())

    def get_prnfile1_url(self, obj):
        return self._build_absolute_url(obj.get_prnfile1_url())

    def get_prnfile2_url(self, obj):
        return self._build_absolute_url(obj.get_prnfile2_url())

    def _build_absolute_url(self, relative_url):
        request = self.context.get('request')
        if relative_url and request:
            return request.build_absolute_uri(relative_url)
        return None


class OrdOrderOmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdOrderOms
        fields = [
            'final_year_delivery1',
            'finaldelvdate1',
            'jobno_oms',
            'prnfile1_url',
            'prnfile2_url',
        ]



class OrdUdfCompleteKSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdUdfCompleteK
        fields = '__all__'

class OrdOrderOmsSerializer(serializers.ModelSerializer):
    udf_info = OrdUdfCompleteKSerializer()

    class Meta:
        model = OrdOrderOms
        fields = '__all__'