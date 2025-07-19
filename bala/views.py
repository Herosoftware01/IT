from django.shortcuts import render
from .models import OrdSampleStatus
# Create your views here.


# def homess(request):
#     all = OrdSampleStatus.objects.filter("image")
#     print(all)
#     return render(request, "homesss.html")


def homess(request):
    images = (
        OrdSampleStatus.objects.using('mssql')
        .filter(img1__isnull=False)
        .exclude(img1='')
    )

    for obj in images:
        print(f"Image: {obj.img1}")

    return render(request, "homesss.html", {"images": images})