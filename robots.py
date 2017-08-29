#coding=utf-8
#不要用我的key乱搞，自己申请去！！！
import requests as r
import time
def API(text,ID):
    URL="http://www.tuling123.com/openapi/api"
    KEY="a9f839d31262419eb5c9708ae39d6ea8"
    data={
            "key": KEY,
            "info": text,
            "userid":ID,
            }
    try:
        re=r.post(URL,data=data).json()
        if re.get('url')!=None:
            return re.get('text')+'\n'+re.get('url')
        elif re.get('list')!=None:
            s=''
            for i in re.get('list'):
                s=s+i['name']+':'+i['info']+'\n'
            return re.get('text')+'\n'+s
        else:
            return re.get('text')
    except:
        return u'识别失败，请关注公众号：趣发现儿'
def sendinfo(key,target,member):
    url='http://112.74.204.232:9999/sendinfo'
    #url = 'http://127.0.0.1:8080/sendinfo'
    data={
        'key':key,
        'target':target,
        'member':member
    }
    try:
        r.post(url,data=data)
    except:
        pass