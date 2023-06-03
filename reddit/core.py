import requests
from os import getenv, getcwd, environ
from os.path import expanduser
from configparser import ConfigParser

__all__ = [

]

class Reddit:
    @classmethod
    def __load_config(self):
        self._config = ConfigParser()
        self._config.read("reddit\data.ini")
        self.__settings = [key for key in self._config["DEFAULT"]]
        return self.__settings
    
    def __init__(self): 
        self.__session = requests.session()
        self.__session.auth = (getenv("reddit_id"), getenv("reddit_secret"))
        self._conf = self.__load_config()

        

#a = Reddit()
#print(a._conf)

config = ConfigParser()
config.read("reddit\data.ini")
print(config["DEFAULT"]["checkForUpdates"])