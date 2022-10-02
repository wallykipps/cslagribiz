from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('batches', BatchViewSet)
router.register('birdsstock', BirdsStockViewSet)
router.register('production', ProductionViewSet)
router.register('eggsinventory', EggsInventoryViewSet)
router.register('products', ProductsViewSet)
router.register('customers', CustomersViewSet)
router.register('sales', SalesViewSet)
router.register('creditsales', CreditSalesViewSet)
router.register('vendors', VendorsViewSet)
router.register('costcategories', CostCategoriesViewSet)
router.register('expenses', ExpensesViewSet)
router.register('creditexpenses', CreditExpensesViewSet)
router.register('vaccinationprogram', VaccinationProgramViewSet)
router.register('weighttargets', WeightTargetsViewSet)
router.register('vaccination', VaccinationViewSet)
router.register('weightmonitoring', WeightMonitoringViewSet)
router.register('stockmovement', StockMovementViewSet)
router.register('cashbalance', CashBalanceViewSet)
router.register('feedtypes', FeedTypesViewSet)
router.register('feedinventory', FeedInventoryViewSet)
router.register('feedtargets', FeedTargetsViewSet)



urlpatterns = router.urls