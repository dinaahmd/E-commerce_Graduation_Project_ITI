from django.shortcuts import render
from .models import ProductItem
from .serializers import ProductItemSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

# CBV Class based views
# List and Create == GET and POST
# class Product_List(APIView):
#     def get(self, request):
#         search_query = request.query_params.get('search', None)
#         if search_query:
#             products = ProductItem.objects.filter(name__icontains=search_query)
#         else:
#             products = ProductItem.objects.all()
#         serializer = ProductItemSerializer(products, many = True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = ProductItemSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status = status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors,
#             status= status.HTTP_400_BAD_REQUEST
#         )
class Product_List(APIView):

    serializer_class = ProductItemSerializer

    def get(self, request):
        products = ProductItem.objects.all()
        serializer = ProductItemSerializer(products, many = True)
        return Response(serializer.data)

    def post(self, request):

        serializer = ProductItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
#GET PUT DELETE cloass based views -- slug

class Product_Details(APIView):
    def get_object(self, id):
        try:
            return ProductItem.objects.get(id=id)
        except ProductItem.DoesNotExist:
            raise Http404
    def get(self, request, id):
        product = self.get_object(id)
        serializer = ProductItemSerializer(product)
        return Response(serializer.data)
    def put(self, request, id):
        product = self.get_object(id)
        serializer = ProductItemSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)