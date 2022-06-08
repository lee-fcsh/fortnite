"""import otree.api"""
from otree.api import *

class C(BaseConstants):
    """Constants for the game"""
    NAME_IN_URL = 'public_goods_simple'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    ENDOWMENT = cu(100)
    MULTIPLIER = 2


class Subsession(BaseSubsession):
    """class that contains the game"""


class Group(BaseGroup):
    """class that contains the players"""
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    """class that contains the players"""
    contribution = models.CurrencyField(
        min=0, max=C.ENDOWMENT, label="How much will you contribute?"
    )


# FUNCTIONS
def set_payoffs(group: Group):
    """function that calculates the payoffs"""
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = (
        group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP
    )
    for player in players:
        player.payoff = C.ENDOWMENT - player.contribution + group.individual_share


# PAGES
class Contribute(Page):
    """page that contains the form"""
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    """page that waits for the other players or the results"""
    after_all_players_arrive = set_payoffs


class Results(Page):
    """page that displays the results"""


page_sequence = [Contribute, ResultsWaitPage, Results]
