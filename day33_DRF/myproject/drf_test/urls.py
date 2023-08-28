from rest_framework.routers import DefaultRouter
from .views import TODOViewSet

router = DefaultRouter()
router.register("drf_test", TODOViewSet)

# 추가시 urlpatterns = router.urls
urlpatterns = router.urls
