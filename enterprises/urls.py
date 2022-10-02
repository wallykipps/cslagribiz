# from django.contrib import admin
# from django.urls import path, include
from rest_framework import routers
from .views import CompanyViewSet,BusinessUnitViewSet,EnterpriseTypeViewSet,StaffViewSet, UserViewSet, BankingViewSet, PaymentModesViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('companies', CompanyViewSet, 'companies')
router.register('businessunits', BusinessUnitViewSet, 'businessunits')
router.register('enterprisetypes', EnterpriseTypeViewSet, 'enterprisetypes')
router.register('staff', StaffViewSet, 'staff')
router.register('payment_modes', PaymentModesViewSet, 'payment_modes')
router.register('banking', BankingViewSet, 'banking')


urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls)),
# ]