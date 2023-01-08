from unittest import mock

from django.test import TestCase
from rest_framework.test import APITestCase

from rock_paper_scissors.models import Turn, Choice
from rock_paper_scissors.serializers import ChoiceSerializer, TurnSerializer
from rock_paper_scissors.views import turn


class TurnTestCase(TestCase):
    def test_paper_beats_rock(self):
        paper = Choice.InnerChoice.PAPER
        rock = Choice.InnerChoice.ROCK

        self.assertEqual(turn(player_choice=paper, ai_choice=rock), Turn(outcome=Turn.Outcome.WIN))

    def test_rock_beats_scissors(self):
        rock = Choice.InnerChoice.ROCK
        scissors = Choice.InnerChoice.SCISSORS

        self.assertEqual(turn(player_choice=rock, ai_choice=scissors), Turn(outcome=Turn.Outcome.WIN))

    def test_scissors_beats_paper(self):
        scissors = Choice.InnerChoice.SCISSORS
        paper = Choice.InnerChoice.PAPER

        self.assertEqual(turn(player_choice=scissors, ai_choice=paper), Turn(outcome=Turn.Outcome.WIN))

    def test_symmetry(self):
        scissors = Choice.InnerChoice.SCISSORS
        paper = Choice.InnerChoice.PAPER

        self.assertEqual(turn(player_choice=scissors, ai_choice=paper), Turn(outcome=Turn.Outcome.WIN))
        self.assertEqual(turn(player_choice=paper, ai_choice=scissors), Turn(outcome=Turn.Outcome.LOSE))

    def test_draw(self):
        scissors = Choice.InnerChoice.SCISSORS

        self.assertEqual(turn(player_choice=scissors, ai_choice=scissors), Turn(outcome=Turn.Outcome.DRAW))


class ServerTestCase(APITestCase):

    @mock.patch('random.choice')
    def test_post_rps(self, mocked_random_choice):
        paper = Choice(choice=Choice.InnerChoice.ROCK)
        choice_serializer = ChoiceSerializer(paper)

        mocked_random_choice.return_value = Choice.InnerChoice.SCISSORS

        response = self.client.post('/rps/', choice_serializer.data, format='json')

        turn_serializer = TurnSerializer(data=response.data)

        self.assertTrue(turn_serializer.is_valid())
        self.assertEqual(turn_serializer.data["outcome"], Turn.Outcome.WIN)

