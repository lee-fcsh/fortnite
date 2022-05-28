
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'blank_app'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    name = models.StringField()
    age = models.IntegerField()
class Survey(Page):
    form_model = 'player'
    form_fields = ['name', 'age']
class Results(Page):
    form_model = 'player'
page_sequence = [Survey, Results]