from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class inicio(Page):
    """Formatos iniciales"""
    form_model = 'player'
    form_fields = ['codigo', 'curso', 'sexo', 'colegio'] # this means player.name, player.age
    def is_displayed(self):
        return self.round_number == 1


class Introduction(Page):
    """Description of the game: How to play and returns expected"""
    def is_displayed(self):
        return self.round_number == 1
    pass

class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


    def vars_for_template(self):
        return {
        'player_in_previous_rounds': self.player.in_previous_rounds(),
        }

class lider(Page):
    """ Aparecerá una vez se llegue a la ronda en la que el líder pueda intervenir"""
    def is_displayed(self):
        return (self.round_number == 3) or (self.round_number == 6) or (self.round_number == 9)

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        group = self.group
        players = group.get_players()
        contributions = [p.contribution for p in players]
        group.total_contribution = min(contributions)
        para_pagos = min(contributions)

        #group.individual_share = group.total_contribution * Constants.multiplier / Constants.players_per_group
        for p in players:
            p.pago = Constants.endowment - p.contribution * Constants.multiplier + (Constants.bono*para_pagos)#cada uno recibe de acuerdo a la funcion con minimo

class AllGroupsWaitPage(WaitPage):
    wait_for_all_groups = True

class para_lider(WaitPage):
    pass

class Results(Page):
    pass

class quiz_final(Page):
    form_model = 'player'
    form_fields = ['rendimiento_grupo',
                   'rendimiento_lider',
                   'juicio_compañeros']
    def is_displayed(self):
        """Preguntas control durante experimento"""
        return (self.round_number == 4) or (self.round_number == 7)
    



page_sequence = [
    inicio,
    AllGroupsWaitPage,
    Contribute,
    ResultsWaitPage,
    Results,
    lider,
    para_lider,
    ]
