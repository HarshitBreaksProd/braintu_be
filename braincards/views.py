from typing import override
from django.db.models import Q
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import BrainCard
from .permissions import IsOwnerOrSharedReadOnly
from .serializers import BrainCardSerializer


class BrainCardViewSet(viewsets.ModelViewSet):
    queryset = BrainCard.objects.all()
    serializer_class = BrainCardSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSharedReadOnly]

    def get_queryset(self):
        return BrainCard.objects.filter(
            Q(owner=self.request.user) | Q(is_shared=True)
        )
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    @action(detail=True, methods=["post"])
    def toggle_share(self, request, pk=None):
        brain_card = self.get_object()
        if brain_card.owner != request.user:
            return Response({"error": "Not allowed"}, status=status.HTTP_403_FORBIDDEN)
        brain_card.is_shared = not brain_card.is_shared
        brain_card.save()
        return Response({"shared": brain_card.is_shared})