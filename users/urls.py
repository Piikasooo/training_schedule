from rest_framework.routers import DefaultRouter
from .views import UserVievSet


router = DefaultRouter()
router.register('users', UserVievSet)

urlpatterns = router.urls