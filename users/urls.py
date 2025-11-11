
from rest_framework.routers import DefaultRouter
from users.views import UserSimpleViewSet


router = DefaultRouter()
router.register(r'', UserSimpleViewSet, basename='user')
urlpatterns = router.urls