from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural="Company"

    def __str__(self):
        return self.company

class EnterpriseType(models.Model):
    type = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural="Enterprise Type"

    def __str__(self):
        return self.type

class BusinessUnit(models.Model):
    unit = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    enterprisetype=models.ForeignKey(EnterpriseType, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="Business Unit"

    def __str__(self):
        return self.unit

class Staff(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phonenumber=models.CharField(max_length=255)
    businessunit=models.ForeignKey(BusinessUnit, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural="Staff"
    def __str__(self):
        return self.firstname

class PaymentModes(models.Model):
    payment_mode = models.CharField(max_length=255)
    name = models.CharField(max_length=255,default='Petty Cash')
    account = models.CharField(max_length=255, default='Ngata_01')

    
    class Meta:
        verbose_name_plural="Payment Mode"

    def __str__(self):
        return self.payment_mode

    def payment_details(self):
        return '%s-%s-%s' %  (self.payment_mode,self.name,self.account)


class Banking(models.Model):
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    account = models.CharField(max_length=255, default='000')
    
    class Meta:
        verbose_name_plural="Banking"

    def __str__(self):
        return '%s-%s-%s' %  (self.type,self.name,self.account)

    def bank_details(self):
        return '%s-%s-%s' %  (self.type,self.name,self.account)