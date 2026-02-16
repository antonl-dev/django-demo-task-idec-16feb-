# api/views.py

from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Note
from .serializers import NoteSerializer, UserSerializer
from .permissions import IsOwner

# For Bonus: Simple Search
from rest_framework.filters import SearchFilter

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    # BONUS: Implemented simple search
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self):
        user = self.request.user
        queryset = Note.objects.filter(owner=user)

        # Handle the `archived` query parameter
        archived_param = self.request.query_params.get('archived')

        if archived_param == 'true':
            queryset = queryset.filter(is_archived=True)
        else:
            # Default behavior: exclude archived notes
            queryset = queryset.filter(is_archived=False)
            
        return queryset.order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
