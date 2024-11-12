
from rest_framework import serializers
from .models import MenuItems
from decimal import Decimal

class MenuItemSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(source = 'title')
    price_after_tax = serializers.SerializerMethodField(method_name='calc_tax')
    class Meta:
        model = MenuItems
        fields = ['id','name','price', 'inventory','price_after_tax', ]
    
    def calc_tax(self, product = MenuItems):
        return product.price * Decimal(1.1)
    