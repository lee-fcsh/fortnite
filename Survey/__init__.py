from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField()
    age = models.IntegerField()


# PAGES
class Survey(Page):
    form_model = 'player'
    form_fields= ['name', 'age']

class Results(Page):
    form_model = 'player'


page_sequence = [Survey, Results]
