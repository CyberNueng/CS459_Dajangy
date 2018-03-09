from rent.models import Customer
from rest_framework import routers, serializers, viewsets

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'phone')