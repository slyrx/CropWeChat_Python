# -*- coding:utf-8 -*-

import random

import requests
import json


def getToken():
    token = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwac92dd00a6ef82d7&corpsecret=Xs57eA5eusOmPTgg-qa8fDrQq3P2Fek9jX0WME6rJvw")
    return token.json().get("access_token")

args = {
    "touser":"LiuHongRu",
    "agentid":1000003,
    "msgtype": "text",
    "climsgid":"climsgidclimsgid_%f"% (random.random()),
    'text':{
        "content":"欢迎来到这里！",
    },
    "safe":0,
}

url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=ACCESS_TOKEN"
url = url.replace("ACCESS_TOKEN", getToken())
post = "POST"


response = requests.post(url, data=json.dumps(args).decode('unicode-escape').encode("utf-8")).json()

print response








