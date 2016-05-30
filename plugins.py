# -*- coding: utf-8 -*-
import re

from slackbot.bot import respond_to
from slackbot.bot import listen_to

from sensors.db.session import DBSession
from sensors.db.models import RoomMetrics


@respond_to(u'^(hi|hello|привет)', re.IGNORECASE)
def hi(message, phrase):
    # react with thumb up emoji
    message.react('+1')
    message.reply("Hello! I'm glad to see you!")


@respond_to(u'(^status|how are you\?|как дела\?)', re.IGNORECASE)
def how_are_you(message, phrase):
    message.reply("Everything is fine. I'm working!\nYou can ask me what I can do in order to know more.")


@respond_to('I love you')
def love(message):
    message.react('heart')
    message.reply('I love you too!')


@respond_to('data', re.IGNORECASE)
def data(message):
    session = DBSession()
    last_metric = session.query(RoomMetrics).order_by(RoomMetrics.appended.desc()).first()
    message.reply("Temperature: {0} *C \nHumidity:     {1} %".format(last_metric.temperature, last_metric.humidity))


@respond_to('stat$', re.IGNORECASE)
@respond_to('stat (.*) (.*)', re.IGNORECASE)
def stats(message, start_date=None, end_date=None):
   message.reply("Sorry, unfortunatelly, I can't return a statistics.")


@respond_to(u'(что ты умеешь делать\?|What can you do\?|help)', re.IGNORECASE)
def help(message, phrase):
    message.reply("""
Hello, I'm zero. I'm a slack bot and I can execute the following commands:

hi (hello, привет) - I can greet you.
status (how are you? как дела?) - I can inform you about my status.
data - I can return the latest information from sensors.
""")
