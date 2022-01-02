import json
from django.http import response
from django.test.utils import setup_test_environment
from rest_framework import serializers, status
from django.test import TestCase, Client, client
from  django.urls import reverse
from rest_framework.response import Response
from .models import CartItem
from .serializers import CartItemSerializer

# initialize the APIClient app
client = Client()


# Create your tests here.

class GetAllCartItem(TestCase):
    """Test module for get all cartitem API"""
    def setUp(self):
        CartItem.objects.create(
            product_quantity=6.0,product_name= 'Product Name 6',product_price= 41.0)
        CartItem.objects.create(
            product_quantity=7.0,product_name= 'Product Name 7',product_price= 42.0)
        CartItem.objects.create(
            product_quantity=8.0,product_name= 'Product Name 8',product_price= 43.0)
    
    def test_get_all_cart_item(self):

        #get API response
        response = client.get('/api/cart-items')

        #get data from db
        items = CartItem.objects.all()
        serializer = CartItemSerializer(items,many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data'],serializer.data )

class GetSingleCartItem(TestCase):
    """Test get single data chart item"""
    def setUp(self):
        self.cart_item = CartItem.objects.create(
            product_quantity=8.0,product_name= 'Product Name 8',product_price= 43.0)
    
    def test_get_single_cart_item(self):
        id = self.cart_item.id;
        url = f'/api/cart-items/{id}'

        #get API response
        response = client.get(url,HTTP_ACCEPT='application/json')

        #get data from db
        items = CartItem.objects.get(id=self.cart_item.id)
        serializer = CartItemSerializer(items)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data'],serializer.data )
