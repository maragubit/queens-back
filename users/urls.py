from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views import RegisterUserViewSet, UserSimpleViewSet


router = DefaultRouter()
router.register(r'', UserSimpleViewSet, basename='user')
register_user = RegisterUserViewSet.as_view({'post': 'register'})
urlpatterns = [
    path('register/', register_user, name='register_user')
    ] + router.urls