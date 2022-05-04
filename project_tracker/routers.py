from rest_framework.routers import DefaultRouter

from projects.viewsets import ProjectGenericViewSet


router = DefaultRouter()
router.register('projects', ProjectGenericViewSet, basename='projects')

print(router.urls)

urlpatterns = router.urls