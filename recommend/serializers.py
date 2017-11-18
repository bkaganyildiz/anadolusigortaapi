from .models import RecommendationResult
from rest_framework import serializers


class RecommendationResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationResult
        fields = ("name", "bayes_values", "mlp_values", "dt_values", "number_of_features", "picture")
