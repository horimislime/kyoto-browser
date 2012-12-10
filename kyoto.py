__author__ = 'horimislime'

import ConfigParser
import kyototycoon
from dataset import KtDataset

class Kyoto:
    def __init__(self):
        self.config=ConfigParser.SafeConfigParser()
        self.config.read('settings.prop')


        for section in self.config.sections():
            if section!='kyototycoon':
                continue

            self.host=self.config.get('kyototycoon','host')
            self.port=self.config.get('kyototycoon','port')

        if self.host is not None and self.port is not None:
            self.kyototycoon=kyototycoon.KyotoTycoon()
            self.kyototycoon.open(host=self.host,port=self.port)

    def get_settings(self):
        return self.host,self.port

    def set_configs(self,host,port):
        self.config.set('kyototycoon','host',host)
        self.config.set('kyototycoon','port',port)

    def get(self,key):
        return self.kyototycoon.get(key)

    def get_datasets(self):
        keys=self.kyototycoon.match_prefix('')
        keys.sort()

        datasets=[]
        for key in keys:
            datasets.append(KtDataset(key,self.kyototycoon.get(key),self.kyototycoon.get(key)))

        return datasets

    def delete(self,key):
        return self.kyototycoon.remove(key)
