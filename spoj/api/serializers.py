from rest_framework import serializers
from .models import Problem

class ProbSerializer(serializers.ModelSerializer):
    class Meta:
        model= Problem
        fields = [
            'name',
            'url',
            'prob_id',
            'tags'
        ]