from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSets, RoleViewSets

router = DefaultRouter()
router.register(r'organization', OrganizationViewSets)
router.register(r'role', RoleViewSets)


urlpatterns = [
    path('', include(router.urls)),
]