
from django.db import router
from rest_framework.routers import DefaultRouter
from teachers.views import TeacherViewSet


router = DefaultRouter()
router.register(r'', TeacherViewSet, basename='teacher')

urlpatterns = router.urls