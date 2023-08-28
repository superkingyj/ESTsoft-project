from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        # examples = {
        #     'id': 100,
        #     'name': "java의 정석",
        #     'price': 38000,
        #     "desc" : "인기 많음"
        # }