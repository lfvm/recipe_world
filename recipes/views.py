
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework import generics
from django.db.models import Q


class RecipeListApiView(APIView):
    serializer_class = RecipeSerializer

    def get(self, request, *args, **kwargs):

        description = request.query_params.get("description", "")
        title = request.query_params.get("title", "")
        tags = request.query_params.get("tags", "")
        tags = tags.split(",") if tags else []


        query = Q()

        if description:
            query |= Q(description__icontains=description)
        if title:
            query |= Q(title__icontains=title)
        if tags:
            query |= Q(tags__id__in=tags)

        recipes = Recipe.objects.filter(query)

        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        data = {
            'description': request.data.get('description'), 
            'user': request.user.id,
            'title': request.data.get('title'),
        }
        serializer = RecipeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    lookup_field = "pk"


