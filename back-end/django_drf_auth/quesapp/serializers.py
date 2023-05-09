from rest_framework import serializers
from quesapp.models.technologies import TechnologyList


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyList
        fields = ['id', 'technology_name']
        