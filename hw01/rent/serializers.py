from rent.models import Customer, Car, Rent
from rest_framework import routers, serializers, viewsets

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    '''
    def create(self,validated_data):
        """test"""
    '''
    def update(self,instance,validated_data):
        """test"""
    '''
    def delete(self,instance):
        """test"""
    '''

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class RentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rent
        fields = ('customer', 'car', 'fee')