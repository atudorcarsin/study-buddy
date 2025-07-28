from .views import ModuleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'modules', ModuleViewSet, basename='module')

urlpatterns = router.urls