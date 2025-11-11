from rest_framework import routers
from django.urls import path
from courses.views import CourseViewSet

router = routers.DefaultRouter()
router.register(r'', CourseViewSet, basename='course')
urlpatterns = router.urls
