from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartItemSerializer
from .models import CartItem
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class CartItemViews(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CartItemSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK) 
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, id=None):
        paginator = LimitOffsetPagination()
        if id:
            item = get_object_or_404(CartItem, id=id)
            serializer = CartItemSerializer(item)
            return Response({"status":"success","data": serializer.data}, status= status.HTTP_200_OK)
        
        items = CartItem.objects.all()
        resultpage = paginator.paginate_queryset(items,request);
        serializer = CartItemSerializer(resultpage, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self,request, id=None):
        item = CartItem.objects.get(id=id)
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
    
    def delete(self, request, id=None):
        item = get_object_or_404(CartItem, id=id)
        item.delete()
        return Response({"status":"success","data": "Data Deleted"})
