from django.shortcuts import render
from .models import ProductItem, ProductCategory
from .serializers import ProductItemSerializer, ProductCategorySerializer
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

# CBV Class based views
# List and Create == GET and POST
class Product_List(APIView):
    def get(self, request):
        search_query = request.query_params.get('search', None)
        if search_query:
            products = ProductItem.objects.filter(name__icontains=search_query)
        else:
            products = ProductItem.objects.all()
        serializer = ProductItemSerializer(products, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ProductItemSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
        )
    
#GET PUT DELETE cloass based views -- slug

# class  Product_Details(APIView):

#     def get_object(self, slug):
#         try:
#             return ProductItem.objects.get(slug=slug)
#         except ProductItem.DoesNotExists:
#             raise Http404
#     def get(self, request, slug):
#         product = self.get_object(slug)
#         serializer = ProductItemSerializer(product)
#         return Response(serializer.data)
#     def put(self, request, slug):
#         product = self.get_object(slug)
#         serializer = ProductItemSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, slug):
#         product = self.get_object(slug)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)