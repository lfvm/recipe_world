from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "created_at", "updated_at", "name"]