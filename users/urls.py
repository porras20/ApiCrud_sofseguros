from django.urls import path, include
from rest_framework import routers
from users import views
# Api version
router = routers.DefaultRouter()
router.register('users',views.UserView, 'users' )
urlpatterns = [
    path('api/v1/', include(router.urls))
]