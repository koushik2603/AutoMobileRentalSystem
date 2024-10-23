from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('clientregistration',views.clientregistration,name="clientregistration"),
    path('clientlogin',views.clientlogin,name="clientlogin"),
    path('checkclientlogin',views.checkclientlogin,name="checkclientlogin"),
    path('clienthome',views.clienthome,name="clienthome"),
    path('clientlogout',views.clientlogout,name="clientlogout"),
    path('addvehicle',views.addvehicle,name="addvehicle"),
    path('viewallvehicles',views.viewallvehicles,name="viewallvehicles"),
    path("viewavehicle", views.viewavehicle, name="viewavehicle"),
    path("displayvehicle", views.displayvehicle, name="displayvehicle"),
    path("payment", views.payment, name="payment"),
path("pay", views.pay, name="pay"),


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
