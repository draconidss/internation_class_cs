SESSION_CONFIGS = [
    {
        'name': 'dictator_game',
        'display_name': "独裁者游戏",
        'num_demo_participants': 2,  # 演示模式人数
        'app_sequence': ['dictator_app'],  # 应用顺序
        'endowment': 100,  # 初始资金（货币单位）
    }
]

SESSION_CONFIG_DEFAULTS = [
    {
        'name': 'dictator_game',
        'display_name': "独裁者游戏",
        'num_demo_participants': 2,  # 演示模式人数
        'app_sequence': ['dictator_app'],  # 应用顺序
        'endowment': 100,  # 初始资金（货币单位）
    }
]

# 货币和语言配置
REAL_WORLD_CURRENCY_CODE = 'CNY'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'ECU'
LANGUAGE_CODE = 'zh-hans'

# 实验参数
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

ROOMS = [
    {
        'name': 'lab',
        'display_name': '实验室',
        'participant_label_file': '_rooms/lab.txt',
    }
]

INSTALLED_APPS = ['otree']