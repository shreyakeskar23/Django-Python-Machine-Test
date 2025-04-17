from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet, UserProjectListAPIView, ClientDeleteAPIView, ProjectDeleteAPIView

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
    path('projects/', UserProjectListAPIView.as_view(), name='user-projects'),
    path('clients/<int:pk>/delete/', ClientDeleteAPIView.as_view(), name='delete-client'),
    path('projects/<int:pk>/delete/', ProjectDeleteAPIView.as_view(), name='delete-project'),
]
from django.urls import path
from .views import ClientDetailView

urlpatterns = [
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
]
# urls.py
from django.urls import path
from .views import ClientDetailView

urlpatterns = [
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
]
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = router.urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet, UserProjectListAPIView

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('my-projects/', UserProjectListAPIView.as_view(), name='user-projects'),
]
