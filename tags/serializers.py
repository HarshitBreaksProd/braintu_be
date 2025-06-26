from rest_framework import serializers

from braintu_be.tags.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields='__all__'