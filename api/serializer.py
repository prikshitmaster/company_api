from rest_framework import serializers

from api.models import Customers, Products


class CustomerSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class ProductSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields= "__all__"


