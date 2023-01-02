from rest_framework import serializers

from rock_paper_scissors.models import Choice, Turn

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

class TurnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turn
        fields = '__all__'
