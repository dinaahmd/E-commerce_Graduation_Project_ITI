from django.urls import path
from .views import Product_List, Product_Details

urlpatterns = [
    path('', Product_List.as_view()),
    path('<int:id>/', Product_Details.as_view()),
]