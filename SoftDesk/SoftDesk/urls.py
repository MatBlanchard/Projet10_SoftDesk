from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from app.views import SignupViewSet,  ProjectViewSet, ContributorsViewSet, IssuesViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()
router.register('', SignupViewSet, basename='signup')
router.register('projects', ProjectViewSet, basename='project')

users_router = routers.NestedSimpleRouter(router, 'projects', lookup="projects", trailing_slash=False)
users_router.register(r"users/?", ContributorsViewSet, basename="users", )

issues_router = routers.NestedSimpleRouter(router, 'projects', lookup="projects", trailing_slash=False)
issues_router.register(r"users/?", IssuesViewSet, basename="issues", )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/', include(users_router.urls)),
    path('api/', include(issues_router.urls)),
]
