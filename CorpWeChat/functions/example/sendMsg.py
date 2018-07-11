# -*- coding:utf-8 -*-

from functions.CoreApi.OperationFramework import *
from functions.conf import conf

myCrop = OperationFramework(conf["corpid"], conf["secret"])

data = {
    "touser":"LiuHongRu",
    "agentid":1000003,
    "msgtype": "text",
    'text':{
        "content":"你好！5",
    },
    "safe":0,
}

print myCrop.sendUrl(CORPWECHAT_DICT["send_application_msg"][0], data)