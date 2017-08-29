# -*- coding: utf-8 -*-
import random
import robots
import Config
def onQQMessage(bot, contact, member, content):
    if '@ME' in content:
        content = robots.API(content.replace('@ME', ''), member.name)
        bot.SendTo(contact, member.name.decode('utf-8') + ':' + content)
        robots.sendinfo(bot.conf.qq,'@ME',member.name)
    elif '好友' in str(contact):
        content = robots.API(content, str(contact))
        bot.SendTo(contact, content)
        robots.sendinfo(str(bot.conf.qq),'frinde','frinde')
    elif getattr(member,'uin',None)!=bot.conf.qq:
        for i in Config.ls:
            if i in content:
                num=Config.ls.index(i)
                target=Config.ls[num]
                n=random.randint(0,len(Config.dic[target])-1)
                print i
                bot.SendTo(contact,Config.dic[target][n],resendOn1202=False)
                #如果一句话中有多个关键词，只是别第一个关键词！
                #可以做一下简单的统计和分析，想想还是记录昵称和内容了。
                robots.sendinfo(bot.conf.qq,'target','Lenovo')
                break
        if '三炮最帅'==content:
            bot.SendTo(contact,'在下阿汇')
