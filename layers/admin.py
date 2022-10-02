from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin

class BatchAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'delivery_date_1', 'batch', 'supplier','ordered_birds','delivered_birds','unitprice','total_cost','status','createdAt')

class BirdsStockAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'stock_date_1', 'stock_movement_type','birds','birds_stock_actual','stock_movement_notes','batch','status','staff','createdAt')

class ProductionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'prod_date_1', 'batch','birds', 'gross', 'defects','broken','gross_crates','net_crates','delivered_birds','gross_percentage','net_percentage','staff','createdAt')

class EggsInventoryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'inventory_date_1', 'batch', 'egg_loss_defects', 'egg_loss_breakages','egg_loss_transport','egg_loss_unaccounted','eggs_stock_actual_crates','eggs_stock_actual_pieces', 'egg_total_losses', 'eggs_stock_actual', 'staff','createdAt')

class CustomersAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'reg_date_1', 'customer_name', 'phonenumber', 'email','location')

class SalesAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'date_1', 'product', 'quantity','unitprice','payment_mode','customer','batch','staff','createdAt')

class CreditSalesAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'instalment_date_1','sale_id','batch','batch_id','date','customer','product','quantity','total_sales', 'instalment_amount', 'payment_mode','recipient','createdAt')

class VendorsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'vendor_date_1', 'vendor', 'phonenumber', 'email','location')

class CostCategoriesAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'cost_category', 'cost_sub_category')

class ExpensesAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'purchase_date_1', 'cost_category', 'vendor', 'expense_details','quantity','unitprice','payment_type','batch','paymentsource','staff','createdAt')

class CreditExpensesAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'instalment_date','instalment_date_1', 'payment_mode', 'payment_source','instalment_amount','createdAt')

class VaccinationProgramAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'week', 'vaccine', 'application_mode')

class WeightTargetsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'week', 'weight_range', 'target_average_weight')

class VaccinationAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'vaccination_date_1', 'vaccination', 'vet_agrovet','comments','batch','implementedby')

class WeightMonitoringAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'weight_date_1', 'weight_week', 'average_weight_target','actual_maximum_weight','actual_minimum_weight','actual_average_weight','batch','measuredby')

class ProductsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'productname', 'unit')

class StockMovementAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'stock_movement_type', 'stock_movement_category')

class CashBalanceAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'deposit_date', 'deposit_date_1','batch','deposit_amount','debit_ac','credit_ac','cash_balance','staff','createdAt')

class FeedTypesAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id','feed_type_1','unit','unitmeasure', 'brand')

class FeedInventoryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'batch','feed_type', 'stock_in','bags_consumed','bags_balance','staff','createdAt')

class FeedTargetsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'feed_type','week','weeks','weekly_feed_per_bird')


admin.site.register(Batch, BatchAdmin)
admin.site.register(BirdsStock, BirdsStockAdmin)
admin.site.register(Production, ProductionAdmin)
admin.site.register(EggsInventory, EggsInventoryAdmin)
admin.site.register(Customers, CustomersAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(CreditSales, CreditSalesAdmin)
admin.site.register(Vendors, VendorsAdmin)
admin.site.register(CostCategories, CostCategoriesAdmin)
admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(CreditExpenses, CreditExpensesAdmin)
admin.site.register(VaccinationProgram, VaccinationProgramAdmin)
admin.site.register(WeightTargets, WeightTargetsAdmin)
admin.site.register(Vaccination, VaccinationAdmin)
admin.site.register(WeightMonitoring, WeightMonitoringAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(StockMovement, StockMovementAdmin)
admin.site.register(CashBalance, CashBalanceAdmin)
admin.site.register(FeedTypes, FeedTypesAdmin)
admin.site.register(FeedInventory, FeedInventoryAdmin)
admin.site.register(FeedTargets, FeedTargetsAdmin)


