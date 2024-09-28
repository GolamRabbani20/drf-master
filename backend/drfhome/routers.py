from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewsets

router = DefaultRouter()
router.register('products', ProductViewsets, basename='product')

urlpatterns = router.urls