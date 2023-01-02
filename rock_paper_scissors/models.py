from django.db import models

class Choice(models.Model):
    """
    Model for possible player choices
    """
    class InnerChoice(models.TextChoices):
        ROCK = "ROCK"
        PAPER = "PAPER"
        SCISSORS = "SCISSORS"

    choice = models.CharField(choices=InnerChoice.choices, max_length=10, primary_key=True)

class Turn(models.Model):
    """
    Model for a turn with its outcome
    """
    class Outcome(models.TextChoices):
        WIN = "win"
        LOSE = "lose"
        DRAW = "draw"

    outcome = models.CharField(choices=Outcome.choices, max_length=4, primary_key=True)
