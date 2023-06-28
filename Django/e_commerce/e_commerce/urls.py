from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/' ,include('products.urls')),
    path('api-auth', include('rest_framework.urls')),
    path('api/', include('base.api.urls'))

]

