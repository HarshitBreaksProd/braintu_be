from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from braintu_be.braincards.permissions import IsOwnerOrSharedReadOnly
from braintu_be.braincards.serializers import BrainCardSerializer
from braintu_be.brainspaces.models import BrainSpace


class BrainSpaceViewset(viewsets.ModelViewSet):
    queryset = BrainSpace.objects.all()
    serializer_class = BrainCardSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSharedReadOnly]

    def get_queryset(self):
        return BrainSpace.objects.filter(
            Q(owner=self.request.user) | Q(is_shared=True)
        )
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    @action(detail=True, methods=["post"])
    def toggle_share(self, request, pk=None):
        brain_space = self.get_object()
        if brain_space.owner != request.user:
            return Response({"error": "Not allowed"}, status=status.HTTP_403_FORBIDDEN)
        brain_space.is_shared = not brain_space.is_shared
        brain_space.save()
        return Response({"shared": brain_space.is_shared})