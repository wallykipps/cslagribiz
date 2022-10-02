from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.contrib.auth.models import User
from .serializers import CompanySerializer, EnterpriseTypeSerializer, BusinessUnitSerializer, StaffSerializer, UserSerializer,PaymentModesSerializer,BankingSerializer
from .models import Company, EnterpriseType, BusinessUnit, Staff, PaymentModes, Banking

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class EnterpriseTypeViewSet(viewsets.ModelViewSet):
    serializer_class = EnterpriseTypeSerializer
    queryset = EnterpriseType.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class BusinessUnitViewSet(viewsets.ModelViewSet):
    serializer_class = BusinessUnitSerializer
    queryset = BusinessUnit.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class PaymentModesViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentModesSerializer
    queryset = PaymentModes.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class BankingViewSet(viewsets.ModelViewSet):
    serializer_class = BankingSerializer
    queryset = Banking.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
