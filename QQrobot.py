# -*- coding: utf-8 -*-
from qqbot import _bot as bot
import plug
if __name__ == '__main__':
    bot.Login()
    bot.conf.Display()
    bot.Plug('plug')
    bot.Run()