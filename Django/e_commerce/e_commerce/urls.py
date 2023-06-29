from django.contrib import admin
from django.urls import path, include
# from products.views import Product_List
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/' ,include('products.urls')),
    path('api/', include('base.api.urls')),
    path('api-auth', include('rest_framework.urls')),
    
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

