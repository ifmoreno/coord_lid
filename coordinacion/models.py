from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv

author = 'Ivan Felipe Moreno'

doc = """
Juego de coordinacion del link más débil. 
"""


class Constants(BaseConstants):
    name_in_url = 'coordinacion'
    players_per_group = 4
#    players_per_group = 2
    num_rounds = 12
   # num_rounds = 6
    endowment = 10
    multiplier = 0.5
    bono = 0.75

    instructions_template = 'coordinacion/Instructions.html'


class Subsession(BaseSubsession):
    def vars_for_admin_report(self):
        contributions = [p.contribution for p in self.get_players() if p.contribution != None]
        if contributions:
            return {
                'avg_contribution': sum(contributions)/len(contributions),
                'min_contribution': min(contributions),
                'max_contribution': max(contributions),
            }
        else:
            return {
                'avg_contribution': '(no data)',
                'min_contribution': '(no data)',
                'max_contribution': '(no data)',
            }



class Group(BaseGroup):
    total_contribution = models.IntegerField()
    print('defined fields on the Group')

class Player(BasePlayer):
    pago = models.FloatField(min=0, max=100)
    para_pagos = models.IntegerField(min=0, max=Constants.endowment)
    contribution = models.IntegerField(
        choices=range(0, 11,2),
        doc="""Agent's work effort, [1, 10]""",
        widget=widgets.Select)
    curso = models.StringField(
        choices=("8a","8b","8c","8d","8e",
                "9a","9b","9c","9d","9e",
                "10a","10b","10c","10d","10e"),
        widget= widgets.Select
    )
    colegio = models.StringField(
        choices=("San Pedro",
                 "San Jose",
                 "Nuestra Senora del Rosario",
                 "Nuestra Senora Presentacion"),
        widget= widgets.Select
    )
    codigo = models.IntegerField(
        choices=range(1,40),
        widget=widgets.Select
    )
    sexo = models.IntegerField(
    choices=[
        [1, 'Masculino'],
        [2, 'Femenino'],
    ])

