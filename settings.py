"""import os"""
from os import environ

SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
SESSION_CONFIGS = [dict(name='app_sequence', num_demo_participants=None, app_sequence=['my_trust'])]
ROOMS = [
    dict(
        name='econ101',
        display_name='Experimental Economics Lab 1',
        participant_label_file='_rooms/participant_label_file_ing.txt',
        use_secure_urls=True
    ),
    dict(
        name='econ102',
        display_name='Experimental Economics Lab 2',
        participant_label_file='_rooms/participant_label_file_med.txt',
        use_secure_urls=True
    ),
    dict(
        name='econ103',
        display_name='Experimental Economics Lab 3',
        participant_label_file='_rooms/participant_label_file_eco.txt',
        use_secure_urls=True
    )
]
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '9673134352672'
