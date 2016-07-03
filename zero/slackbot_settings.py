API_TOKEN = ''
ERRORS_TO = ''
DEFAULT_REPLY = "Sorry but I didn't understand you"

DHT11_PIN = 7

PLUGINS = [
    'slackbot.plugins',
    'plugins',
]

try:
	from local_settings import *
except:
	pass