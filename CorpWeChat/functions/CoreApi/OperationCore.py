import requests


class OperationException(Exception):
    def __init__(self, errCode, errMsg):
        self.errCode = errCode
        self.errMsg = errMsg

class OperationAbstractApi(object):
    def __init__(self):
        return

    def getToken(self, url, tokenType):
        return  requests.get(url).json().get(tokenType)

    def send(self, url, data):
        return requests.post(url, data=data).json()