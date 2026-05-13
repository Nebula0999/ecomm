from rest_framework import serializers
from .models import category, Product

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'  

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'