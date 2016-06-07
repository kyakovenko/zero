API_TOKEN = ''
ERRORS_TO = ''
DEFAULT_REPLY = "Sorry but I didn't understand you"


PLUGINS = [
    'slackbot.plugins',
    'plugins',
]

try:
	from .local_settings import *
except:
	pass