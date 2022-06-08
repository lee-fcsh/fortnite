"""import otree.api"""
from otree.api import *

class C(BaseConstants):
    """constants for the game"""
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    """class that contains the game"""


class Group(BaseGroup):
    """class that contains the players"""


class Player(BasePlayer):
    """class that contains the players"""
    name = models.StringField()
    age = models.IntegerField()


# PAGES
class Survey(Page):
    """page that contains the form"""
    form_model = 'player'
    form_fields= ['name', 'age']

class Results(Page):
    """page that displays the results"""
    form_model = 'player'


page_sequence = [Survey, Results]
