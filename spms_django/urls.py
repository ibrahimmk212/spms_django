from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from institute.views import FacultyViewSet, DepartmentViewSet
from project.views import AllocationViewSet,AllocationReadWriteViewSet

router = routers.DefaultRouter()
router.register(r'faculties', FacultyViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'allocation', AllocationViewSet)
router.register(r'allocationrw', AllocationReadWriteViewSet)


# Additionally, we include login URLs for the browsable API.f
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('accounts/', include('account.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/auth/', CustomAuthToken.as_view())
]
