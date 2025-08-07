from otree.api import *
from .models import *

# 游戏介绍页
class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1  # 仅第一轮显示

# 决策页（仅独裁者可见）
class OfferPage(Page):
    form_model = 'group'
    form_fields = ['dictator_decision']
    
    @staticmethod
    def is_displayed(player: Player):
        return player.role() == '独裁者'  # 仅独裁者决策

# 结果等待页
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'  # 所有人到齐后计算收益
    
    @staticmethod
    def set_payoffs(group: Group):
        for p in group.get_players():
            p.set_payoff()

# 结果展示页
class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        return {
            'dictator_decision': group.dictator_decision,
            'kept': C.ENDOWMENT - group.dictator_decision
        }

page_sequence = [Introduction, OfferPage, ResultsWaitPage, Results]