from Shop.models import Customer, Item, Purchase, Cart
from rest_framework.serializers import ModelSerializer


class Customerserializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class Itemserializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class Purchaseserializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class Cartserializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'