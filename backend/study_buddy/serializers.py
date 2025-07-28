from rest_framework.serializers import ModelSerializer

from study_buddy.models import Module


class ModuleSerializer(ModelSerializer):
    class Meta:
        model = Module
        fields = ['name', 'description', 'is_favorite']

