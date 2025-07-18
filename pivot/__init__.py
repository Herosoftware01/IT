# admin_utils.py or inside admin.py
from django.urls import path, reverse
from django.http import JsonResponse
from django.template.response import TemplateResponse
from decimal import Decimal
from django.contrib import admin

class PivotTableMixin(admin.ModelAdmin):
    pivot_fields = []  # Optional override in child class

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['pivot_url'] = reverse(f'admin:{self.model._meta.app_label}_{self.model._meta.model_name}_pivot')
        return super().changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        base_urls = super().get_urls()
        opts = self.model._meta
        custom_urls = [
            path('pivot/', self.admin_site.admin_view(self.pivot_view),
                 name=f'{opts.app_label}_{opts.model_name}_pivot'),
            path('pivot-data/', self.admin_site.admin_view(self.pivot_data),
                 name=f'{opts.app_label}_{opts.model_name}_pivot_data'),
        ]
        return custom_urls + base_urls

    def pivot_view(self, request):
        model = self.model
        app_label = model._meta.app_label
        model_name = model._meta.model_name
        

        # Show all fields (columns), excluding 'id'
        all_fields = [f.name for f in model._meta.fields if f.name != 'id']

        model_meta = {
            'app_label': app_label,
            'model_name': model_name,
            'fields': all_fields
        }

        pivot_data_url = reverse(f'admin:{app_label}_{model_name}_pivot_data')

        context = dict(
            self.admin_site.each_context(request),
            title=f'{model._meta.verbose_name_plural.title()} Pivot Table',
            model_meta=model_meta,
            pivot_data_url=pivot_data_url
        )

        return TemplateResponse(request, "admin/universal_pivot.html", context)

    def pivot_data(self, request):
        # Show all fields (columns)
        fields = self.pivot_fields if self.pivot_fields else [f.name for f in self.model._meta.fields if f.name != 'id']
        # Show all rows
        queryset = self.model.objects.using('mssql').all()
        data = []
        for obj in queryset:
            row = {}
            for field in fields:
                value = getattr(obj, field, None)
                # If the value is a method, call it
                if callable(value):
                    value = value()
                # Handle Decimal values
                if isinstance(value, Decimal):
                    value = float(value)
                # Convert datetime to string if needed
                if hasattr(value, 'strftime'):
                    value = value.strftime('%Y-%m-%d %H:%M:%S')
                row[field] = value
            data.append(row)
        return JsonResponse(data, safe=False)


