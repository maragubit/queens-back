from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views import RegisterUserViewSet, UserSimpleViewSet, register_user


router = DefaultRouter()
router.register(r'', UserSimpleViewSet, basename='user')
registerUser = RegisterUserViewSet.as_view({'post': 'register'})
urlpatterns = [
    path('register/', registerUser, name='register_user'),
    path("register_link/", registerUser, name="register_link"),
    ] + router.urls