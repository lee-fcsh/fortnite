"""File containing the my_trust application logic,
are the classes, constants and functions that are executed when starting the app."""
from otree.api import *
doc = """
app that contains a teo forms, one for the 1st player to send points(10 max), and the other one for the 2nd player.
"""
class C(BaseConstants):
    """Constants for the game"""
    NAME_IN_URL = 'my_trust'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    ENDOWMENT = cu(10)
    MULTIPLICATION_FACTOR = 3

class Subsession(BaseSubsession):
    """class that contains the game"""


class Group(BaseGroup):
    """class that contains the players"""
    sent_amount = models.CurrencyField(
        label="How much do you want to send to participant B?"
    )
    sent_back_amount = models.CurrencyField(
        label="How much do you want to send back?"
    )


class Player(BasePlayer):
    """class that contains the players"""
    sent_amount = models.CurrencyField()
    sent_back_amount = models.CurrencyField()

def sent_back_amount_choices(group):
    """function that calculates the choices for the sent back amount
    Args: 
        group: Group
    Return: list of choices
    """
    return currency_range(
        0,
        group.sent_amount * C.MULTIPLICATION_FACTOR,
        1
    )
def set_payoffs(group: Group):
    """function that calculates the payoffs
    Args: 
        group: Group
    Return: None
    """
    player1 = group.get_player_by_id(1)
    player2 = group.get_player_by_id(2)
    player1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
    player2.payoff = group.sent_amount * C.MULTIPLICATION_FACTOR - group.sent_back_amount
# PAGES
class Send(Page):
    """page that contains the form"""
    form_model = 'group'
    form_fields = ['sent_amount']

    @staticmethod
    def is_displayed(player):
        """function that determines whether the page is displayed
        Args:
            player: Player
        Return: boolean
        """
        return player.id_in_group == 1

class WaitForP1(WaitPage):
    """page that waits for the other player"""

class SendBack(Page):
    """page that contains the form"""
    form_model = 'group'
    form_fields = ['sent_back_amount']

    @staticmethod
    def is_displayed(player):
        """function that determines whether the page is displayed
        Args:
            player: Player
        Return: boolean
        """
        return player.id_in_group == 2

    @staticmethod
    def vars_for_template(player):
        """function that determines the variables for the template
        Args:
            player: Player
        Return: dictionary
        """
        group = player.group

        return dict(
            tripled_amount=group.sent_amount * C.MULTIPLICATION_FACTOR
        )

class ResultsWaitPage(WaitPage):
    """page that waits for the other players or the results"""
    after_all_players_arrive = set_payoffs
class Results(Page):
    """page that displays the results"""


page_sequence = [Send, WaitForP1, SendBack, ResultsWaitPage, Results]
