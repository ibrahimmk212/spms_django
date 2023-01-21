from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from authentication.authentication import CustomAuthToken
from institute.views import FacultyViewSet, DepartmentViewSet, SessionViewSet
from project.views import AllocationViewSet, ChapterApprovalUpdateView, StudentMyDetailView, CountView,GenerateProposalViewSet,StudentProposalView, ChapterApprovalViewSet, AllocationReadWriteViewSet, ProposalViewSet, GradingViewSet, GradingRWViewSet

router = routers.DefaultRouter()
router.register(r'faculties', FacultyViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'allocation', AllocationViewSet)
router.register(r'allocationrw', AllocationReadWriteViewSet)
router.register(r'proposals', ProposalViewSet)
router.register(r'chapterapproval', ChapterApprovalViewSet)
router.register(r'grading', GradingViewSet)
router.register(r'gradingrw', GradingRWViewSet)
router.register(r'generateallocation', GenerateProposalViewSet)


# Additionally, we include login URLs for the browsable API.f
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('accounts/', include('account.urls')),
    path('count/', CountView.as_view()),
    path('studentmydetail/<int:student_id>/', StudentMyDetailView.as_view()),
    path('studentchapters/<int:proposal>/', ChapterApprovalUpdateView.as_view()),
    path('myproposal/<int:student_id>/', StudentProposalView.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/', CustomAuthToken.as_view())
]
