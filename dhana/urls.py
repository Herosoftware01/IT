
# from django.contrib import admin
# from django.urls import path,include
# from .import views
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('home', views.home, name='home'),
#     path('api/print', views.PrintRgbAltViewSet, name='PrintRgbAltViewSet'),
#     path('', views.images1, name='images1'),
#     ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrintRgbAltViewSet,get_order_data,stream_order_data,orders,OrderWithUdfAPIView,order_data_api,order_delivery
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'print', PrintRgbAltViewSet, basename='print')

urlpatterns = [
    # path('home/', home, name='home'),
    # path('', images1, name='images1'),
    path('api/', include(router.urls)),  
    path('api/order-data/', get_order_data),
    path('orders/', orders, name='orders'),
    path('astream_order_data/', stream_order_data, name='stream_order_data'),
    path('api/orders/', OrderWithUdfAPIView.as_view(), name='order-udf-api'),
    path('api/order_data_api/', order_data_api, name='order_data_api'),
    path('api/order_delivery/', order_delivery, name='order_delivery'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


