from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.views import SignupViewSet, LoginViewSet, LogoutViewSet,  ProjectViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()
router.register('', SignupViewSet, basename='signup')
router.register('', LoginViewSet, basename='login')
router.register('', LogoutViewSet, basename='logout')
router.register('projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]
