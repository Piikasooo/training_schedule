from rest_framework.routers import DefaultRouter
from .views import UserViewSet


router = DefaultRouter()
router.register('api', UserViewSet)

urlpatterns = router.urls