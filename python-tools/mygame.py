"""Silly game, mostly to show interactive mode."""

from random import randint


def print_score(score):
    """Print the winning message and score."""

    print("You win! Your score is", score)


score = randint(1, 100)

print_score(score)
