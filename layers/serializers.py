from rest_framework import serializers
from django.db.models import Avg, Count, Min, Sum, Window, F
from layers.admin import VaccinationProgramAdmin
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import urllib.request


class BatchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Batch
        fields = ('id', 'delivery_date','delivery_date_1', 'batch', 'supplier','breed','ordered_birds','delivered_birds','unitprice','status','total_cost', 'businessunit','enterprisetype','business_unit','enterprise_type','createdAt')


class StockMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMovement
        fields = ('id', 'stock_movement_type', 'stock_movement_category')


class BirdsStockSerializer(serializers.ModelSerializer):
    # birds_stock_balance = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = BirdsStock
        fields = ('id', 'stock_date','stock_date_1','delivered_birds','stock_movement_type','stock_type','stock_description','birds','birds_stock_actual','stock_movement_notes','batch','batch_number','delivery_date','status','staff','staff_','business_unit','enterprise_type','createdAt')


class ProductionSerializer(serializers.ModelSerializer):
    # broken_sum=serializers.SerializerMethodField()
    # defects_all_sum=serializers.SerializerMethodField()
       
    class Meta:
        model = Production
        # fields = ('__all__')
        fields = ('id', 'prod_date','prod_date_1','delivered_birds','batch','batch_number','birds','gross', 'defects','broken','gross_crates','net_crates','gross_percentage','net_percentage','staff','staff_','business_unit','enterprise_type','createdAt')

    # def get_broken_sum(self, obj):
    #     return Production.objects.aggregate(Sum('broken')).get('broken__sum')

    # def get_defects_all_sum(self, obj):
    #     defects=Production.objects.aggregate(Sum('defects')).get('defects__sum')
    #     broken = Production.objects.aggregate(Sum('broken')).get('broken__sum')
    #     defects_all=defects+broken
    #     return defects_all


class EggsInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EggsInventory
        fields = ('id','inventory_date', 'inventory_date_1','batch_number', 'batch', 'egg_loss_defects', 'egg_loss_breakages','egg_loss_transport','egg_loss_unaccounted','eggs_stock_actual_crates','eggs_stock_actual_pieces', 'egg_total_losses', 'eggs_stock_actual', 'staff','staff_','business_unit','enterprise_type','createdAt')

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'productname', 'unit')

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('id', 'reg_date','reg_date_1', 'customer_name', 'phonenumber', 'email','location')


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ('id', 'date', 'date_1', 'product', 'product_','unit','quantity','unitprice','total_sales','payment_mode','paymentmode','customer','customer_name','batch', 'batch_number','staff','staff_','business_unit','enterprise_type','createdAt')

class CreditSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditSales
        # fields = ('id', 'instalment_date_1', 'sale_id','batch','date','customer','product','quantity','total_sales', 'instalment_amount', 'payment_mode','recipient','createdAt')
        fields = ('id','instalment_date', 'instalment_date_1','sale' ,'sale_id', 'batch_id','batch','batch_id','date','customer_id','customer','product','product_','quantity','total_sales', 'payment_mode','paymentmode', 'instalment_amount','paymentmode_','recipient','staff','createdAt')


class VendorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = ('id', 'vendor_date','vendor_date_1', 'vendor', 'phonenumber', 'email','location')

class CostCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCategories
        fields = ('id', 'cost_category','cost_sub_category')

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ('id', 'purchase_date','purchase_date_1', 'cost_category','cost_category_', 'expense_category','expense_sub_category','vendor','supplier', 'expense_details','unit','unit_','brand','unitmeasure_','quantity','unitprice','payment_type','payment_mode','batch','batch_number','delivery_date','payment_point','paymentsource','payment_source','staff','staff_','business_unit','enterprise_type','createdAt')

class CreditExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditExpenses
        fields = ('id', 'instalment_date', 'instalment_date_1', 'expense','payment_mode', 'instalment_amount','payment_source','paymentby','createdAt','batch_id','batch', 'purchase_date', 'cost_id', 'vendor_id', 'vendor', 'quantity','unit_price','paymentmode', 'cost_category', 'cost_category_','cost_details', 'total_cost', 'paymentmode_', 'paymentsource', 'staff')

class CashBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashBalance
        fields = ('id', 'deposit_date','deposit_date_1','batch','batch_number','deposit_amount','debit_ac','credit_ac','credit_ac_details','debit_ac_details','cash_balance','staff','staff_','createdAt')

class FeedTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedTypes
        fields = ('id', 'feed_type_1','feed_type','unit','unitmeasure', 'brand')

class FeedInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedInventory
        fields = ('id','stock_date','stock_date_1', 'batch','batch_number','delivery_date','feed_type','feed_type_1','purchased_bags','unit','brand','stock_in','bags_consumed','bags_balance','staff','staff_','createdAt')


class VaccinationProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationProgram
        fields = ('id', 'vaccine_regimen','week', 'vaccine','vaccination_day', 'application_mode')

class WeightTargetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightTargets
        fields = ('id', 'week', 'weight_range', 'target_average_weight')

class VaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = ('id', 'vaccination_date', 'vaccination_date_1', 'vaccination', 'vaccine_regimen','vaccine','vaccination_day','vet_agrovet','comments','batch','batch_number','delivery_date','implementedby','staff')

class WeightMonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightMonitoring
        fields = ('id', 'weight_date','weight_date_1', 'week','weight_week', 'average_weight_target','actual_maximum_weight','actual_minimum_weight','actual_average_weight','batch','batch_number','measuredby','staff')

class FeedTargetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedTargets
        fields = ('id', 'feed_type','feed_type_1','week','weeks','weekly_feed_per_bird')

