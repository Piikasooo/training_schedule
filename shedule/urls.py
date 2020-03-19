from rest_framework.routers import DefaultRouter
from .views import TaskViewSet


router = DefaultRouter()
router.register('training', TaskViewSet)

urlpatterns = router.urls