from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv

author = 'Ivan'

doc = """
questionario inicial
"""

class Constants(BaseConstants):
    name_in_url = 'quiz_inicial'
    players_per_group = None

    with open('prueba/quiz.csv') as questions_file:
        questions = list(csv.DictReader(questions_file))

    num_rounds = len(questions)
    instructions_template = 'coordinacion/Instructions.html'

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['questions'] = Constants.questions.copy()

        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = int(question_data['id'])
            p.question = question_data['question']
            p.solution = question_data['solution']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_id = models.IntegerField()
    question = models.StringField()
    solution = models.StringField()
    submitted_answer = models.StringField(widget=widgets.RadioSelect)
    is_correct = models.BooleanField()

    def current_question(self):
        return self.session.vars['questions'][self.round_number - 1]

    def check_correct(self):
        self.is_correct = (self.submitted_answer == self.solution)
