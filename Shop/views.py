from django.shortcuts import render
from Shop.models import Customer, Item, Purchase,Cart
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from Shop.serializers import Customerserializer, Itemserializer, Purchaseserializer, Cartserializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = Customerserializer
class UserPPDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = Customerserializer
    lookup_field = 'id'


class ItemListCreateAPIView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = Itemserializer
    lookup_field = 'id'


class ItemPPDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = Itemserializer
    lookup_field = 'id'


class PurchaseListCreateAPIView(ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = Purchaseserializer
    lookup_field = 'id'


class PurchasePPDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = Purchaseserializer
    lookup_field = 'id'


class CartListCreateAPIView(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = Cartserializer
    lookup_field = 'id'


class CartPPDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = Cartserializer
    lookup_field = 'id'


# Create your views here.
