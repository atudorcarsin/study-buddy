from rest_framework.viewsets import ModelViewSet

from study_buddy.models import Module
from study_buddy.serializers import ModuleSerializer


class ModuleViewSet(ModelViewSet):
    serializer_class = ModuleSerializer

    def get_queryset(self):
        return Module.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)