from multiprocessing.dummy import active_children
from django.db.models.query_utils import select_related_descend
from django.db.models import Avg, Count, Min, Sum, Window, F, Q, Case, When, Value
from django.db.models.functions import ExtractYear
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.contrib.auth.models import User
from .serializers import *
from .models import *
import pandas as pd
import numpy as np
from django_pandas.io import read_frame


class BatchViewSet(viewsets.ModelViewSet):
    serializer_class = BatchSerializer
    queryset = Batch.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class BirdsStockViewSet(viewsets.ModelViewSet):
    serializer_class = BirdsStockSerializer
    queryset = BirdsStock.objects.filter(batch__status=True)

    # birds_stock_update = BirdsStock.objects.filter(stock_movement_type__stock_movement_category='Stock Out')
    # birds_stock_update.update(birds=F('birds') * -1)
    #Aggregate running balance
    # queryset = BirdsStock.objects.filter(batch__status=True).annotate(
    #     birds_stock_balance=Window(
    #         Sum('birds'),
    #         partition_by=[F('batch')],
    #         order_by=F('stock_date').asc()
    #     )
    # ).order_by('-batch','stock_date','birds_stock_balance')

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


   
class ProductionViewSet(viewsets.ModelViewSet):
    serializer_class = ProductionSerializer
    queryset = Production.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     return Production.objects.annotate(
    #         total_defects=Sum('defects'),
    #         total_broken=Sum('broken')
    #     )


class EggsInventoryViewSet(viewsets.ModelViewSet):
    serializer_class = EggsInventorySerializer
    queryset = EggsInventory.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CustomersViewSet(viewsets.ModelViewSet):
    serializer_class = CustomersSerializer
    queryset = Customers.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class SalesViewSet(viewsets.ModelViewSet):
    serializer_class = SalesSerializer
    queryset = Sales.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class CreditSalesViewSet(viewsets.ModelViewSet):
    serializer_class = CreditSalesSerializer
    queryset = CreditSales.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class VendorsViewSet(viewsets.ModelViewSet):
    serializer_class = VendorsSerializer
    queryset = Vendors.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class CostCategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CostCategoriesSerializer
    queryset = CostCategories.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class ExpensesViewSet(viewsets.ModelViewSet):
    serializer_class = ExpensesSerializer
    queryset = Expenses.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class CreditExpensesViewSet(viewsets.ModelViewSet):
    serializer_class = CreditExpensesSerializer
    queryset = CreditExpenses.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class VaccinationProgramViewSet(viewsets.ModelViewSet):
    serializer_class = VaccinationProgramSerializer
    queryset = VaccinationProgram.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class WeightTargetsViewSet(viewsets.ModelViewSet):
    serializer_class = WeightTargetsSerializer
    queryset = WeightTargets.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class VaccinationViewSet(viewsets.ModelViewSet):
    serializer_class = VaccinationSerializer
    queryset = Vaccination.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class WeightMonitoringViewSet(viewsets.ModelViewSet):
    serializer_class = WeightMonitoringSerializer
    queryset = WeightMonitoring.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class StockMovementViewSet(viewsets.ModelViewSet):
    serializer_class = StockMovementSerializer
    queryset = StockMovement.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class CashBalanceViewSet(viewsets.ModelViewSet):
    serializer_class = CashBalanceSerializer
    queryset = CashBalance.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class FeedTypesViewSet(viewsets.ModelViewSet):
    serializer_class = FeedTypesSerializer
    queryset = FeedTypes.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class FeedInventoryViewSet(viewsets.ModelViewSet):
    serializer_class = FeedInventorySerializer
    queryset = FeedInventory.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class FeedTargetsViewSet(viewsets.ModelViewSet):
    serializer_class = FeedTargetsSerializer
    queryset = FeedTargets.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)