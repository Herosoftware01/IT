from django.shortcuts import render
from .models import VueYarnStock,PrintRgbAlt
import pandas as pd
import pygwalker as pyg
from pygwalker import to_html

from pygwalker import walk


# Create your views here.
# def home(request):
#     data = VueYarnStock.objects.all()
#     return render(request, "home.html", {"data":data})


def home(request):
    data = VueYarnStock.objects.using('mssql').all()
    return render(request, "home.html", {"data": data})



# def dashboard(request):
#     queryset = PrintRgbAlt.objects.using('mssql').all()
#     data = list(queryset.values())
#     df = pd.DataFrame(data)
    
#     if 'img_print' in df.columns:
#         df['img_print'] = df['img_print'].apply(
#             lambda url: f'<img src="{url}" width="80" height="80">' if pd.notna(url) else ''
#         )
#     pyg_html = pyg.to_html(df, dark='light', render_image=True)
      # pyg_html = df.to_html(escape=False)
#     return render(request, 'dashboard.html', {'pyg_html': pyg_html})


def dashboard(request):
    queryset = PrintRgbAlt.objects.using('mssql').all()
    data = list(queryset.values())
    df = pd.DataFrame(data)

    # Optional: show image preview
    if 'img_print' in df.columns:
        df['img_print'] = df['img_print'].apply(
            lambda url: f'<img src="{url}" width="80" height="80">' if pd.notna(url) else ''
        )

    # Example pivot (replace columns accordingly)
    if 'job_number' in df.columns and 'img_print' in df.columns:
        pivot_df = pd.pivot_table(df, index='job_number', values='img_print', aggfunc=lambda x: ', '.join(x))

        table_html = pivot_df.to_html(escape=False)
    else:
        table_html = df.to_html(escape=False)

    return render(request, 'dashboard.html', {'table_html': table_html})




# def dashboard(request):
#     queryset = PrintRgbAlt.objects.using('mssql').all()
#     data = list(queryset.values())
#     df = pd.DataFrame(data)

#     # Don't convert to <img> tags — Pygwalker needs raw URL
#     pyg_html = walk(df, return_html=True)  # returns interactive UI

#     return render(request, 'dashboard.html', {'pyg_html': pyg_html})



