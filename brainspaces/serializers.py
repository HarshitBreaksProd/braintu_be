from rest_framework import serializers
from braintu_be.brainspaces.models import BrainSpace

class BrainSpaceSerializer(serializers.ModelField):
    class Meta:
        model = BrainSpace
        fields = '__all__'
        read_only_field = ['owner']