from rest_framework import serializers
from .models import Banking, Company, BusinessUnit, EnterpriseType, PaymentModes,Staff 
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs ={'password': {"write_only": True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'company', 'location')

class EnterpriseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseType
        fields = ('id', 'type', 'category')

class BusinessUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUnit
        fields = ('id', 'unit', 'location','company','enterprisetype')

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff 
        fields = ('id', 'firstname', 'lastname','phonenumber','businessunit')

class PaymentModesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModes
        fields = ('id', 'payment_mode','name','account','payment_details')

class BankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banking 
        fields = ('id', 'type','name','account','bank_details')