from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OrganizationSerializer, RoleSerializer
from .models import Organization, Role


class OrganizationViewSets(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class RoleViewSets(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer    

