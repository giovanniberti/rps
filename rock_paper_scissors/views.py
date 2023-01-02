import random
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from rock_paper_scissors.models import Choice, Turn
from rock_paper_scissors.serializers import ChoiceSerializer, TurnSerializer
from loguru import logger

class RockPaperScissorsView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        choice_serializer = ChoiceSerializer(data=data)

        if not choice_serializer.is_valid():
            return Response({ "error": choice_serializer.error_messages }, status=status.HTTP_400_BAD_REQUEST)

        player_choice = choice_serializer.data["choice"]
        ai_choice = random.choice(list(Choice.InnerChoice))

        turn_outcome = turn(player_choice=player_choice, ai_choice=ai_choice)
        turn_serializer = TurnSerializer(turn_outcome)

        logger.info("Player played {} while AI played {}. Player outcome={}", player_choice, ai_choice, turn_outcome.outcome)

        return Response(turn_serializer.data)

def turn(player_choice, ai_choice):
    ROCK = Choice.InnerChoice.ROCK
    PAPER = Choice.InnerChoice.PAPER
    SCISSORS = Choice.InnerChoice.SCISSORS

    if player_choice == ai_choice:
        return Turn(outcome=Turn.Outcome.DRAW)
    elif (player_choice, ai_choice) == (PAPER, ROCK) or \
        (player_choice, ai_choice) == (ROCK, SCISSORS) or \
        (player_choice, ai_choice) == (SCISSORS, PAPER):
        return Turn(outcome=Turn.Outcome.WIN)

    return Turn(outcome=Turn.Outcome.LOSE)
