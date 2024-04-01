
from rest_framework import permissions
from .models import Tag
from rest_framework import generics
from .serializers import TagSerializer

class TagListCreateView(generics.ListCreateAPIView):
    
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

  


class TagRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    lookup_field = "pk"


