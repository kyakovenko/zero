# -*- coding: utf-8 -*-
import sys
import logging
from slackbot.bot import Bot

logging.getLogger('slackbot').addHandler(logging.StreamHandler(sys.stdout))


def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
