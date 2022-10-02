from django.db import models
from django_pandas.managers import DataFrameManager
# from django_pandas.io import read_framepip 
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from enterprises.models import EnterpriseType, BusinessUnit, Staff, Banking, PaymentModes

#1 Batch/Day Old Chicks
class Batch(models.Model):
    delivery_date = models.DateField()
    batch = models.CharField(max_length=255, blank=False, null=False, default='N/A')
    supplier = models.CharField(max_length=255, blank=False, null=False)
    breed = models.CharField(max_length=255, blank=True, null=True)
    ordered_birds=models.IntegerField(validators=[MinValueValidator(0)])
    delivered_birds=models.IntegerField(validators=[MinValueValidator(0)])
    unitprice = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    status=models.BooleanField(default=True)
    businessunit = models.ForeignKey(BusinessUnit, verbose_name="businessunit", on_delete=models.CASCADE)
    enterprisetype = models.ForeignKey(EnterpriseType, verbose_name="enterprisetype", on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    objects = DataFrameManager()

    class Meta:
        ordering=["delivery_date"]
        verbose_name_plural="Batches"

    def __str__(self):
        return self.batch

    def delivery_date_1(self):
        return self.delivery_date.strftime('%e-%b-%y')

    def total_cost(self):
        total_cost =(self.ordered_birds*self.unitprice)
        return total_cost

    def business_unit(self):
        return self.businessunit.unit

    def enterprise_type(self):
        return self.enterprisetype.type



#2 Stock movement types
class StockMovement(models.Model):
    stock_movement_type = models.CharField(max_length=255)
    stock_movement_category = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural="Stock Movement Types"

    def __str__(self):
        return '%s-%s' %  (self.stock_movement_category,self.stock_movement_type)
    
#3 Birds stock
class BirdsStock(models.Model):
    stock_date=models.DateField()
    stock_movement_type=models.ForeignKey(StockMovement, verbose_name="stock_movement_type", on_delete=models.CASCADE)
    birds =models.IntegerField(default=0)
    birds_stock_actual=models.IntegerField(default=0)
    stock_movement_notes=models.CharField(max_length=255,blank=True, null=True)
    batch=models.ForeignKey(Batch, verbose_name="batch", on_delete=models.CASCADE)
    staff=models.ForeignKey(Staff, verbose_name="staff", on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    objects = DataFrameManager()

    class Meta:
        ordering=["batch"]
        verbose_name_plural="Birds Stock"

    def stock_date_1(self):
        return self.stock_date.strftime('%e-%b-%y')

    def batch_number(self):
        return self.batch.batch

    def delivery_date(self):
        return self.batch.delivery_date

    def status(self):
        return self.batch.status

    def stock_type(self):
        return self.stock_movement_type.stock_movement_category

    def stock_description(self):
        return self.stock_movement_type.stock_movement_type

    def delivered_birds(self):
        return self.batch.delivered_birds

    def business_unit(self):
        return self.batch.businessunit.unit

    def enterprise_type(self):
        return self.batch.enterprisetype.type

    def staff_(self):
        return self.staff.firstname

#4 Production
class Production(models.Model):
    prod_date=models.DateField()
    birds=models.IntegerField(validators=[MinValueValidator(0)], default=1000)
    gross=models.IntegerField(validators=[MinValueValidator(0)])
    defects=models.IntegerField(validators=[MinValueValidator(0)])
    broken=models.IntegerField(validators=[MinValueValidator(0)])
    batch=models.ForeignKey(Batch, verbose_name="batch", on_delete=models.CASCADE)
    # birds=models.ForeignKey(BirdsStock, verbose_name="birds", on_delete=models.CASCADE, default=1)
    # birds=models.ManyToManyField('birds')
    staff=models.ForeignKey(Staff, verbose_name="staff", on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    objects = DataFrameManager()

    class Meta:
        ordering=["prod_date"]
        verbose_name_plural="Production"

    def prod_date_1(self):
        return self.prod_date.strftime('%e-%b-%y')

    def batch_number(self):
        return self.batch.batch

    def net(self):
        nett=self.gross-self.defects-self.broken
        return nett

    def gross_crates(self):
        gross_crates=self.gross/30
        return gross_crates

    def net_crates(self):
        nett_crates=(self.gross-self.defects-self.broken)/30
        return nett_crates

    def delivered_birds(self):
        return self.batch.delivered_birds

    def gross_percentage(self):
        gross_percentage=(self.gross/self.birds)*100
        return gross_percentage

    def net_percentage(self):
        nett_percentage=((self.gross-self.defects-self.broken)/self.birds)*100
        return nett_percentage

    def business_unit(self):
        return self.batch.businessunit.unit

    def enterprise_type(self):
        return self.batch.enterprisetype.type

    def staff_(self):
        return self.staff.firstname

   

#5 Eggs Inventory
class EggsInventory(models.Model):
    inventory_date=models.DateField()
    egg_loss_defects=models.IntegerField(null=True,blank=True,default=0)
    egg_loss_breakages=models.IntegerField(null=True,blank=True,default=0)
    egg_loss_transport=models.IntegerField(null=True,blank=True,default=0)
    egg_loss_unaccounted=models.IntegerField(null=True,blank=True,default=0)
    eggs_stock_actual_crates=models.IntegerField(validators=[MinValueValidator(0)],default=0)
    eggs_stock_actual_pieces=models.IntegerField(validators=[MinValueValidator(0)],default=0)
    batch=models.ForeignKey(Batch, verbose_name="batch", on_delete=models.CASCADE)
    staff=models.ForeignKey(Staff, verbose_name="staff", on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    objects = DataFrameManager()
    class Meta:
        ordering=["inventory_date"]
        verbose_name_plural="Eggs Inventory"

    def inventory_date_1(self):
        return self.inventory_date.strftime('%e-%b-%y')

    def batch_number(self):
        return self.batch.batch

    def staff_(self):
        return self.staff.firstname

    def egg_total_losses(self):
        egg_total_losses=self.egg_loss_defects+self.egg_loss_breakages+self.egg_loss_unaccounted
        return egg_total_losses

    def eggs_stock_actual(self):
        eggs_stock_actual=self.eggs_stock_actual_crates+(self.eggs_stock_actual_pieces/30)
        return eggs_stock_actual

    def business_unit(self):
        return self.batch.businessunit.unit

    def enterprise_type(self):
        return self.batch.enterprisetype.type

#6 Products
class Products(models.Model):
    productname = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural="Products"

    def __str__(self):
        return '%s-%s' %  (self.productname,self.unit)


#7 Customers
class Customers(models.Model):
    reg_date=models.DateField()
    customer_name=models.CharField(max_length=255, default="N/A")
    phonenumber=models.CharField(max_length=10, blank=True, null=True, default="N/A")
    email=models.EmailField(max_length=255, blank=True, null=True, default="notapplicable@gmail.com")
    location=models.CharField(max_length=255, blank=True, null=True, default="N/A")
    objects = DataFrameManager()

    class Meta:
        db_table="layers_customers"
        ordering=["reg_date"]
        verbose_name_plural="Customers"
    
    def __str__(self):
        return self.customer_name

    def reg_date_2(self):
        return self.reg_date.strftime('%F')

    def reg_date_1(self):
        return self.reg_date.strftime('%e-%b-%y')


#8 Sales
class Sales(models.Model):
    date=models.DateField()
    product=models.ForeignKey(Products, verbose_name="product", on_delete=models.CASCADE)
    
    # PRODUCT_CHOICES = [
    #     ('', 'Product'),
    #     ('Eggs', 'Eggs'),
    #     ('Ex-layers', 'Ex-layers'),
    #     ('Manure', 'Manure'),
    #     ]
    # product = models.CharField(
    #     max_length=15,
    #     choices=PRODUCT_CHOICES,
    #     default='',
    # )

    # UNIT_CHOICES = [
    #     ('', 'Unit'),
    #     ('Pieces', 'Pieces'),
    #     ('Crates', 'Crates'),
    #     ('Bags', 'Bags'),
    #     ('Kgs', 'Kgs'),
    #     ]
    # unit = models.CharField(
    #     max_length=15,
    #     choices=UNIT_CHOICES,
    #     default='',
    # )

    quantity=models.DecimalField(max_digits=5, decimal_places=2)
    unitprice=models.DecimalField(max_digits=5, decimal_places=2)
    payment_mode=models.ForeignKey(PaymentModes, verbose_name="payment_mode", on_delete=models.CASCADE)


    # PAYMENT_MODE_CHOICES = [
    #     ('', 'Payment Mode'),
    #     ('Cash', 'Cash'),
    #     ('M-Pesa Till', 'M-Pesa Till'),
    #     ('Equitel', 'Equitel'),
    #     ('Bank', 'Bank'),
    #     ('Credit', 'Credit'),
    #     ]
    # payment_mode = models.CharField(
    #     max_length=15,
    #     choices=PAYMENT_MODE_CHOICES,
    #     default='',
    # )

    customer=models.ForeignKey(Customers, verbose_name="customer", on_delete=models.CASCADE)
    batch=models.ForeignKey(Batch, verbose_name="batch", on_delete=models.CASCADE)
    staff=models.ForeignKey(Staff, verbose_name="staff", on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    objects = DataFrameManager()

    class Meta:
        ordering=["date"]
        verbose_name_plural="Sales"

    def __str__(self):
        return '%s-%s-%s-%s %s-%s' % (self.date.strftime('%d-%b-%y'), self.customer,self.payment_mode,self.quantity,self.product.unit,self.quantity*self.unitprice)

    def date_1(self):
        return self.date.strftime('%d-%b-%y')

    def product_(self):
        return self.product.productname
    
    def unit(self):
        return self.product.unit

    def total_sales(self):
        total_sales= self.quantity*self.unitprice
        return round(total_sales,2)

    def total_quantity(self): # To be used for inventory calculation
        if self.product.unit == 'Eggs':
            if self.product.unit=='Pieces':
                total_quantity=round(self.quantity/30,2)
        else:
           total_quantity=self.quantity

        return total_quantity

    def batch_number(self):
        return self.batch.batch

    def customer_name(self):
        return self.customer.customer_name

    def paymentmode(self):
        # return self.payment_mode.payment_mode
        return '%s-%s-%s' %  (self.payment_mode.payment_mode,self.payment_mode.name,self.payment_mode.account)
        

    def staff_(self):
        return self.staff.firstname

    def business_unit(self):
        return self.batch.businessunit.unit

    def enterprise_type(self):
        return self.batch.enterprisetype.type


#9 Credit sales
class CreditSales(models.Model):
    instalment_date=models.DateField()
    sale=models.ForeignKey(Sales, verbose_name="creditsale", on_delete=models.CASCADE)
    instalment_amount=models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    payment_mode=models.ForeignKey(PaymentModes, verbose_name="payment_mode", on_delete=models.CASCADE)

    
    # PAYMENT_MODE_CHOICES = [
    #     ('', 'Payment Mode'),
    #     ('Cash', 'Cash'),
    #     ('M-Pesa Till', 'M-Pesa Till'),
    #     ('Equitel', 'Equitel'),
    #     ('Bank', 'Bank'),
    #     ]
    # payment_mode = models.CharField(
    #     max_length=15,
    #     choices=PAYMENT_MODE_CHOICES,
    #     default='',
    # )

    recipient=models.ForeignKey(Staff, verbose_name="recipient", on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    objects = DataFrameManager()

    class Meta:
        ordering=["instalment_date"]
        verbose_name_plural="Credit Sales"

    def instalment_date_1(self):
        return self.instalment_date.strftime('%e-%b-%y')

    def batch_id(self):
        return self.sale.batch.id

    def batch(self):
        return self.sale.batch.batch

    def date(self):
        return self.sale.date

    def sale_id(self):
        return self.sale.id

    def customer_id(self):
        return self.sale.customer.id

    def customer(self):
        return self.sale.customer.customer_name

    def quantity(self):
        return self.sale.quantity

    def paymentmode(self):
        return self.sale.payment_mode.payment_mode

    def paymentmode_(self):
        # return self.payment_mode.payment_mode
        return '%s-%s-%s' %  (self.payment_mode.payment_mode,self.payment_mode.name,self.payment_mode.account)

    def product(self):
        return '%s-%s' %  (self.sale.product.productname,self.sale.product.unit)

    def product_(self):
        return self.sale.product.productname

    def total_sales(self):
        total_sales= self.sale.quantity*self.sale.unitprice
        return round(total_sales,2)

    def staff(self):
        return self.recipient.firstname

#10 Vendors
class Vendors(models.Model):
    vendor_date=models.DateField()
    vendor=models.CharField(max_length=255,blank=True, null=True)
    phonenumber=models.CharField(max_length=10,blank=True, null=True)
    email=models.EmailField(max_length=255, blank=True, null=True)
    location=models.CharField(max_length=255, blank=True)
    objects = DataFrameManager()

    class Meta:
        ordering=["-vendor_date"]
        verbose_name_plural="Vendors"

    def vendor_date_1(self):
        return self.vendor_date.strftime('%e-%b-%y')

    def __str__(self):
        return self.vendor

#11 Expenses Categories
class CostCategories(models.Model):
    cost_category=models.CharField(max_length=255)
    cost_sub_category=models.CharField(max_length=255, default='')

    objects = DataFrameManager()

    class Meta:
        ordering=["id"]
        verbose_name_plural="Cost Categories"

    def __str__(self):
        return self.cost_sub_category
        # return '%s-%s' %  (self.cost_category,self.cost_sub_category)


#19 Feed Types
class FeedTypes(models.Model):
    # feed_type=models.CharField(max_length=30,blank=True, null=True)
    feed_type_1=models.ForeignKey(CostCategories, verbose_name="feed_type", on_delete=models.CASCADE,blank=True, null=True)
    unit=models.CharField(max_length=30,blank=True, null=True)
    unitmeasure=models.IntegerField(null=True,blank=True)
    brand=models.CharField(max_length=30,blank=True, null=True)

    objects = DataFrameManager()

    class Meta:
        verbose_name_plural="Feed Types"

    def __str__(self):
        # return self.unit
        return '%s-%s-%s-%s' %  (self.feed_type_1,self.unit, self.unitmeasure,self.brand)

    def feed_type(self):
        return self.feed_type_1.cost_sub_category


#12 Expenses
class Expenses(models.Model):
    purchase_date=models.DateField()
    cost_category=models.ForeignKey(CostCategories, verbose_name="cost category", on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendors, verbose_name="vendor", on_delete=models.CASCADE,blank=True)
    expense_details=models.CharField(max_length=255)
    unit=models.ForeignKey(FeedTypes, verbose_name="unit", on_delete=models.CASCADE, default=1,blank=True)
    quantity=models.DecimalField(max_digits=10, decimal_places=2)
    unitprice=models.DecimalField(max_digits=10, decimal_places=2)
    payment_type=models.ForeignKey(PaymentModes, verbose_name="payment_mode", on_delete=models.CASCADE)

    # PAYMENT_TYPE_CHOICES = [
    #     ('', 'Payment Type'),
    #     ('Cash', 'Cash'),
    #     ('Bank', 'Bank'),
    #     ('M-Pesa Till', 'M-Pesa Till'),
    #     ('Equitel', 'Equitel'),
    #     ('Credit', 'Credit'),
    #     ]
    # payment_type = models.CharField(
    #     max_length=15,
    #     choices=PAYMENT_TYPE_CHOICES,
    #     default='',
    # )

    batch=models.ForeignKey(Batch, verbose_name="paymentpoint", related_name='paymentfor',  on_delete=models.CASCADE)
    paymentsource=models.ForeignKey(Batch, verbose_name="paymentsource", related_name='paymentfrom', on_delete=models.CASCADE)
    staff=models.ForeignKey(Staff, verbose_name="staff", on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    objects = DataFrameManager()

    class Meta:
        ordering=["purchase_date"]
        verbose_name_plural="Expenses"

    def batch_number(self):
        return self.batch.batch

    def delivery_date(self):
        return self.batch.delivery_date
        
    
    def total_cost(self):
        total= self.quantity*self.unitprice
        return total

    def purchase_date_1(self):
        return self.purchase_date.strftime('%e-%b-%y')

    def cost_category_(self):
        # return self.cost_category.cost_sub_category
        return self.cost_category.cost_category


    def expense_category(self):
        # return self.cost_category.cost_sub_category
        return '%s-%s' %  (self.cost_category.cost_category,self.cost_category.cost_sub_category)

    def expense_sub_category(self):
        return self.cost_category.cost_sub_category

    def supplier(self):
        return self.vendor.vendor

    def unit_(self):
        return self.unit.unit
        # return '%s-%s' %  (self.unit.unitmeasure,self.unit.unit)

    def unitmeasure_(self):
        return self.unit.unitmeasure
    #     # return '%s-%s' %  (self.unit.unitmeasure,self.unit.unit)

    def brand(self):
        return self.unit.brand

    def payment_mode(self):
        # return self.payment_type.payment_mode
        return '%s-%s-%s' %  (self.payment_type.payment_mode,self.payment_type.name,self.payment_type.account)

    def staff_(self):
        return self.staff.firstname

    def payment_point(self):
        return self.batch.batch

    def payment_source(self):
        return self.paymentsource.batch

    def business_unit(self):
        return self.batch.businessunit.unit

    def enterprise_type(self):
        return self.batch.enterprisetype.type


#13 Credit expenses
class CreditExpenses(models.Model):
    instalment_date=models.DateField()
    expense=models.ForeignKey(Expenses, verbose_name="creditexpense", on_delete=models.CASCADE)
    instalment_amount=models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    payment_mode=models.ForeignKey(PaymentModes, verbose_name="payment_mode", on_delete=models.CASCADE)
    payment_source=models.ForeignKey(Batch, verbose_name="payment_source", related_name='payment_from', on_delete=models.CASCADE, default=27)
    paymentby=models.ForeignKey(Staff, verbose_name="paymentby", on_delete=models.CASCADE, default=27)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    objects = DataFrameManager()

    class Meta:
        ordering=["instalment_date"]
        verbose_name_plural="Credit Expenses"

    def instalment_date_1(self):
        return self.instalment_date.strftime('%e-%b-%y')

    # def credit_expense(self):
    #     if self.expense.payment_type == 'Credit':
    #         credit_expense=self.sale
    #     return credit_expense

    def batch_id(self):
        return self.expense.batch.id
    
    def batch(self):
        return self.expense.batch.batch

    def purchase_date(self):
        return self.expense.purchase_date

    def cost_id(self):
        return self.expense.id

    def vendor_id(self):
        return self.expense.vendor.id

    def vendor(self):
        return self.expense.vendor.vendor

    def unit_price(self):
        return self.expense.unitprice

    def quantity(self):
        return self.expense.quantity

    def paymentmode(self):
        return self.expense.payment_type.payment_mode

    def cost_category(self):
        return '%s-%s' %  (self.expense.cost_category.cost_category,self.expense.cost_category.cost_sub_category)


    def cost_category_(self):
        return self.expense.cost_category.cost_category

    def cost_details(self):
        return self.expense.expense_details
    
    def total_cost(self):
        total_cost= self.expense.quantity*self.expense.unitprice
        return round(total_cost,2)

    def paymentmode_(self):
        # return self.payment_mode.payment_mode.payment_mode
        return '%s-%s-%s' %  (self.payment_mode.payment_mode,self.payment_mode.name,self.payment_mode.account)

    def paymentsource(self):
        return self.payment_source.batch

    def staff(self):
        return self.paymentby.firstname


#14 Vaccination program
class VaccinationProgram(models.Model):
    vaccine_regimen=models.IntegerField(validators=[MinValueValidator(0)],default=0)
    week=models.CharField(max_length=100,blank=True, null=True)
    vaccination_day=models.IntegerField(validators=[MinValueValidator(0)], default=0)
    vaccine=models.CharField(max_length=100,blank=True, null=True)
    application_mode=models.CharField(max_length=255,blank=True, null=True)
    objects = DataFrameManager()

    class Meta:
        verbose_name_plural="Vaccination Program"

    def __str__(self):
        return self.vaccine


#15 Weight Targets
class WeightTargets(models.Model):
    week=models.IntegerField(validators=[MinValueValidator(0)])
    weight_range=models.CharField(max_length=10,blank=True, null=True)
    target_average_weight=models.DecimalField(max_digits=10, decimal_places=2)
    objects = DataFrameManager()
    
    class Meta:
        verbose_name_plural="Weight Targets"

    def __int__(self):
        return self.week


#16 Vaccination
class Vaccination(models.Model):
    vaccination_date=models.DateField()
    vaccination=models.ForeignKey(VaccinationProgram, verbose_name="vaccination", on_delete=models.CASCADE)
    vet_agrovet=models.CharField(max_length=100,blank=True, null=True)
    comments=models.CharField(max_length=100,blank=True, null=True)
    batch=models.ForeignKey(Batch, verbose_name="batch", on_delete=models.CASCADE)
    implementedby=models.ForeignKey(Staff, verbose_name="implementedby", on_delete=models.CASCADE)
    objects = DataFrameManager()
    
    class Meta:
        ordering=["vaccination_date"]
        verbose_name_plural="Vaccination"

    def __str__(self):
        return self.vaccination.vaccine

    def vaccination_date_1(self):
        return self.vaccination_date.strftime('%e-%b-%y')

    def vaccine_regimen(self):
        return self.vaccination.vaccine_regimen

    def vaccine(self):
        return self.vaccination.vaccine

    def delivery_date(self):
        return self.batch.delivery_date.strftime('%e-%b-%y')

    def batch_number(self):
        return self.batch.batch

    def vaccination_day(self):
        return self.vaccination.vaccination_day
       
    def staff(self):
        return self.implementedby.firstname


#17 Weight Monitoring
class WeightMonitoring(models.Model):
    weight_date=models.DateField()
    week=models.ForeignKey(WeightTargets, verbose_name="week", on_delete=models.CASCADE)
    actual_maximum_weight=models.DecimalField(max_digits=10, decimal_places=2)
    actual_minimum_weight=models.DecimalField(max_digits=10, decimal_places=2)
    actual_average_weight=models.DecimalField(max_digits=10, decimal_places=2)
    batch=models.ForeignKey(Batch, verbose_name="batch", on_delete=models.CASCADE)
    measuredby=models.ForeignKey(Staff, verbose_name="measuredby", on_delete=models.CASCADE)
    objects = DataFrameManager()
    
    class Meta:
        ordering=["weight_date"]
        verbose_name_plural="Weight Monitoring"

    # def __str__(self):
    #     return self.week.week

    def weight_date_1(self):
        return self.weight_date.strftime('%e-%b-%y')

    def weight_week(self):
        return self.week.week
    
    def average_weight_target(self):
        return self.week.target_average_weight

    def batch_number(self):
        return self.batch.batch
       
    def staff(self):
        return self.measuredby.firstname


#18 Cash Balance Deposit 
class CashBalance(models.Model):
    deposit_date=models.DateField()
    batch=models.ForeignKey(Batch, verbose_name="batch", on_delete=models.CASCADE)
    deposit_amount=models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    credit_ac=models.ForeignKey(Banking, verbose_name="credit_ac", related_name ='credit_ac', on_delete=models.CASCADE, blank=True, null=True, default=1)
    debit_ac=models.ForeignKey(Banking, verbose_name="debit_ac", related_name ='debit_ac',on_delete=models.CASCADE, blank=True, null=True,default=1)
    cash_balance=models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    staff=models.ForeignKey(Staff, verbose_name="staff", on_delete=models.CASCADE, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    objects = DataFrameManager()
    class Meta:
        ordering=["deposit_date"]
        verbose_name_plural="Cash Deposit"

    def deposit_date_1(self):
        return self.deposit_date.strftime('%e-%b-%y')

    def batch_number(self):
        return self.batch.batch
    
    def credit_ac_details(self):
        return '%s-%s-%s' %  (self.credit_ac.type,self.credit_ac.name,self.credit_ac.account)
        # return self.banking.name

    def debit_ac_details(self):
        return '%s-%s-%s' %  (self.debit_ac.type,self.debit_ac.name,self.debit_ac.account)
        # return self.banking.name
        
    def staff_(self):
        return self.staff.firstname

    def business_unit(self):
        return self.batch.businessunit.unit

    def enterprise_type(self):
        return self.batch.enterprisetype.type

#20 Feed Inventory
class FeedInventory(models.Model):
    stock_date=models.DateField()
    batch=models.ForeignKey(Batch, verbose_name="batch", on_delete=models.CASCADE)
    feed_type=models.ForeignKey(Expenses, verbose_name="feed_type", on_delete=models.CASCADE)
    stock_in=models.DecimalField(max_digits=10, decimal_places=2,default=0,blank=True, null=True)
    # stock_out=models.DecimalField(max_digits=10, decimal_places=2,default=0,blank=True, null=True)
    bags_consumed=models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)
    bags_balance=models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)
    staff=models.ForeignKey(Staff, verbose_name="staff", on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    objects = DataFrameManager()

    class Meta:
        ordering=["stock_date"]
        verbose_name_plural="Feeds Inventory"

    # def __str__(self):
    #     return self.feed_type.unit.feed_type_1

    def stock_date_1(self):
        return self.stock_date.strftime('%e-%b-%y')

    def batch_number(self):
        return self.batch.batch
    
    def delivery_date(self):
        return self.batch.delivery_date

    def feed_type_1(self):
        return self.feed_type.cost_category.cost_sub_category

    def purchased_bags(self):
        return self.feed_type.quantity

    def unit(self):
        # return '%s-%s' %  (self.feed_type,self.banking.bank_type)
        return '%s%s' %  (self.feed_type.unit.unitmeasure,self.feed_type.unit.unit)

    def brand(self):
        # return '%s-%s' %  (self.feed_type,self.banking.bank_type)
        return self.feed_type.unit.brand

    def staff_(self):
        return self.staff.firstname


#21 Feed Targets
class FeedTargets(models.Model):
    feed_type=models.ForeignKey(CostCategories, verbose_name="feed_type", on_delete=models.CASCADE)
    week=models.CharField(max_length=100,blank=True, null=True, default='1')
    weeks=models.IntegerField(validators=[MinValueValidator(0)], default=1)
    weekly_feed_per_bird=models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name_plural="Feed Targets"

    def feed_type_1(self):
        return self.feed_type.cost_sub_category








