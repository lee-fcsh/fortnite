"""File containing the Survey application logic,
are the classes, constants and functions that are executed when starting the app."""
# pylint: disable=import-error
from otree.api import *

# pylint: disable = too-few-public-methods

# pylint: disable=invalid-name
doc = """
app that contains a form with two text field(name, age) and a submit button.
"""

# pylint: disable=invalid-name
# pylint: disable=undefined-variable
class C(BaseConstants):
    """constants for the game"""
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

# pylint: disable=undefined-variable
class Subsession(BaseSubsession):
    """class that contains the game"""

# pylint: disable=undefined-variable
class Group(BaseGroup):
    """class that contains the players"""

# pylint: disable=undefined-variable
class Player(BasePlayer):
    """class that contains the players"""
    name = models.StringField()
    age = models.IntegerField()


# PAGES
# pylint: disable=undefined-variable
class Survey(Page):
    """page that contains the form"""
    form_model = 'player'
    form_fields= ['name', 'age']

# pylint: disable=undefined-variable
class Results(Page):
    """page that displays the results"""
    form_model = 'player'


page_sequence = [Survey, Results]
