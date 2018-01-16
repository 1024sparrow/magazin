from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    #title = serializers.CharField(max_length=200)
    #descr = serializers.CharField(max_length=2048, allow_blank=True)
    class Meta:
        model = Product
        fields = '__all__'
