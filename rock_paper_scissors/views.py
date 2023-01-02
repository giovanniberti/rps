import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rock_paper_scissors.models import Choice, Turn
from rock_paper_scissors.serializers import ChoiceSerializer, TurnSerializer
from loguru import logger

class RockPaperScissorsView(APIView):
    """
    Main view to implement playing Rock, Paper, Scissors.
    """
    def post(self, request):
        """
        API endpoint to play Rock, Paper, Scissors.
        Request body should be deserializable to a :any:`~rock_paper_scissors.models.Choice`
        """
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

def turn(player_choice: Choice.InnerChoice, ai_choice: Choice.InnerChoice) -> Turn:
    """
    Compute a turn outcome for a player against an AI given two choices, following these rules:
     * Paper beats Rock
     * Rock beats Scissors
     * Scissors beats Paper
     * Equal choices are a draw
    """
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
