__author__ = 'horimislime'

class KtDataset:
    def __init__(self,key,value,expireDate):
        self.key=key
        self.value=value
        self.expireDate=expireDate

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def getExpireDate(self):
        return self.expireDate

