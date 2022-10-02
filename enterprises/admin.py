from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin

class CompanyAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id','company', 'location')

class BusinessUnitAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id','unit', 'location','company','enterprisetype')

class EnterpriseTypeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id','type', 'category' )
    
class StaffAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id','firstname', 'lastname','phonenumber','businessunit' )

class PaymentModesAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id','payment_mode','name','account','payment_details')

class BankingAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id','type','name', 'account','bank_details')


admin.site.register(Company, CompanyAdmin)
admin.site.register(BusinessUnit, BusinessUnitAdmin)
admin.site.register(EnterpriseType, EnterpriseTypeAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(PaymentModes, PaymentModesAdmin)
admin.site.register(Banking, BankingAdmin)

