
from OperationCore import *
import json

CORPWECHAT_DICT = {
    "get_access_token":["https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRECT", "GET"],
    "send_application_msg":["https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=ACCESS_TOKEN","POST"]
}
class OperationFramework(OperationAbstractApi):
    def __init__(self, corpid, corpsecret):
        self.corpid = corpid
        self.corpsecret = corpsecret
        return

    def getAccessToken(self):
        return self.getToken(CORPWECHAT_DICT["get_access_token"][0].replace("ID", self.corpid).replace("SECRECT", self.corpsecret), "access_token")

    def sendUrl(self, url, data):
        return self.sendData(url.replace("ACCESS_TOKEN", self.getAccessToken()), data)

    def sendData(self, url, data):
        return self.send(url, json.dumps(data).decode('unicode-escape').encode("utf-8"))
