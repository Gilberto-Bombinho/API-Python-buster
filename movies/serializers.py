from rest_framework import serializers
from .models import RatingChoice, Movie, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(default=None)
    synopsis = serializers.CharField(default=None)
    rating = serializers.ChoiceField(
        choices=RatingChoice.choices, default=RatingChoice.DEFAULT
    )
    added_by = serializers.CharField(read_only=True, source="user.email")
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True, source="movie.title")
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.CharField(read_only=True, source="user.email")
    buyed_at = serializers.DateTimeField(read_only=True)
    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
    
