# -*- coding: utf-8 -*-
import re

from slackbot.bot import listen_to
from slackbot.bot import respond_to

from sensors.db.session import DBSession
from sensors.db.models import RoomMetrics

from netifaces import interfaces, ifaddresses, AF_INET, AF_INET6


@respond_to(u'^(hi|hello)', re.IGNORECASE)
def hi(message, phrase):
    # react with thumb up emoji
    message.react('+1')
    message.reply("Hello! I'm glad to see you!")


@respond_to(u'(^status$|how are you\?)', re.IGNORECASE)
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
    if last_metric:
        message.reply("Temperature: {0} *C \nHumidity:     {1} %".format(last_metric.temperature, last_metric.humidity))
    else:
        message.reply("There is no data.")


@respond_to(u'(where are you\?|^detect_place$)', re.IGNORECASE)
def detect_place(message, phrase):
    addrs = {}
    for interface in interfaces():
        if interface not in ['lo', 'lo0', 'awdl0']:
            info = ifaddresses(interface)
            ip4 = info.get(AF_INET, [{}])[0].get('addr', None)
            ip6 = info.get(AF_INET6, [{}])[0].get('addr', None)
            if ip4 or ip6:
                addrs[interface] = [ip4, ip6]
    if addrs:
        body = '\n'.join(
            '    - {0}\n'\
            '        ipv4: {1}\n'\
            '        ipv6: {2}'.format(
                i, a[0], a[1]
            ) for i, a in addrs.items()
        )
        message.reply('My network settings:\n' + body)


@respond_to('stat$', re.IGNORECASE)
@respond_to('stat (.*) (.*)', re.IGNORECASE)
def stats(message, start_date=None, end_date=None):
   message.reply("Sorry, unfortunatelly, I can't return a statistics.")


@respond_to('test', re.IGNORECASE)
def test(message):
    message.reply(str(dir(message)))


@respond_to(u'(What can you do\?|^help$)', re.IGNORECASE)
def help(message, phrase):
    message.reply("""
Hello, I'm zero. I'm a slack bot and I can execute the following commands:

hi (hello) - I can greet you.
status (how are you?) - I can inform you about my status.
detect_place (where are you?) - I can say you my network settings using which you can connect to me.
data - I can return the latest information from sensors.
""")
