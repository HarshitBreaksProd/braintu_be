from rest_framework import serializers
from .models import BrainSpace

class BrainSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrainSpace
        fields = '__all__'
        read_only_field = ['owner']