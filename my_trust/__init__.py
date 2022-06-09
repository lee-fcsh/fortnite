"""File containing the my_trust application logic,
are the classes, constants and functions that are executed when starting the app."""
#pylint: disable=import-error
from otree.api import *

# pylint: disable = too-few-public-methods

#pylint: disable=invalid-name
doc = """
app that contains a teo forms, one for the 1st player to send points(10 max), and the other one for the 2nd player.
"""

#pylint: disable=invalid-name
#pylint: disable=undefined-variable
class C(BaseConstants):
    """Constants for the game"""
    NAME_IN_URL = 'my_trust'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    ENDOWMENT = cu(10)
    MULTIPLICATION_FACTOR = 3

#pylint: disable=undefined-variable
class Subsession(BaseSubsession):
    """class that contains the game"""

#pylint: disable=undefined-variable
class Group(BaseGroup):
    """class that contains the players"""
    sent_amount = models.CurrencyField(
        label="How much do you want to send to participant B?"
    )
    sent_back_amount = models.CurrencyField(
        label="How much do you want to send back?"
    )

#pylint: disable=undefined-variable
class Player(BasePlayer):
    """class that contains the players"""
    sent_amount = models.CurrencyField()
    sent_back_amount = models.CurrencyField()

def sent_back_amount_choices(group):
    """function that calculates the choices for the sent back amount
    Args:
        group: Group
    Return: list of choices
    >>> sent_back_amount_choices(group) recive 4 points, the range is from 0 to 12
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
#pylint: disable=undefined-variable
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
        >>> is_displayed(player) recive playerid 1, the page is displayed
        """
        return player.id_in_group == 1

#pylint: disable=undefined-variable
class WaitForP1(WaitPage):
    """page that waits for the other player"""

#pylint: disable=undefined-variable
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
        >>> is_displayed(player) recive playerid 2, the page is displayed
        """
        return player.id_in_group == 2

    @staticmethod
    def vars_for_template(player):
        """function that determines the variables for the template
        Args:
            player: Player
        Return: dictionary
        >>> vars_for_template(player) recive 4 pints, the range is from 0 to 12
        """
        group = player.group

        return dict(
            tripled_amount=group.sent_amount * C.MULTIPLICATION_FACTOR
        )

#pylint: disable=undefined-variable
class ResultsWaitPage(WaitPage):
    """page that waits for the other players or the results"""
    after_all_players_arrive = set_payoffs

#pylint: disable=undefined-variable
class Results(Page):
    """page that displays the results"""


page_sequence = [Send, WaitForP1, SendBack, ResultsWaitPage, Results]
