
from students.views import StudentViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
urlpatterns=router.urls
