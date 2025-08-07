from otree.api import *
import settings

class C(BaseConstants):
    NAME_IN_URL = 'dictator_app'
    PLAYERS_PER_GROUP = 2  # 每组2人（独裁者+接受者）
    NUM_ROUNDS = 1
    ENDOWMENT = cu(settings.SESSION_CONFIGS[0]['endowment'])  # 初始资金

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    # 独裁者分配金额
    dictator_decision = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="请决定分配多少金额给对方:"
    )

class Player(BasePlayer):
    # 参与者角色（自动分配）
    def role(self):
        return '独裁者' if self.id_in_group == 1 else '接受者'
    
    # 计算收益
    def set_payoff(self):
        if self.role() == '独裁者':
            self.payoff = C.ENDOWMENT - self.group.dictator_decision
        else:
            self.payoff = self.group.dictator_decision