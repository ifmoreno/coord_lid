from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants




class pregunta_final(Page):
    form_model = 'player'
    form_fields = ['rendimiento_grupo',
                   'rendimiento_lider',
                   'juicio_compañeros']


page_sequence = [
    pregunta_final
]
