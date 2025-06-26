from rest_framework import serializers
from .models import BrainCard

class BrainCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrainCard
        fields = '__all__'
        read_only_field = ['owner']