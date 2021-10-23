# -*- coding: UTF-8 -*-
import os

import yaml
from config import setting
from .logger import Logger
from configparser import ConfigParser

logger = Logger('file_process').getLog()

class ReadFileData(object):
    '''
    读取文件
    '''
    def __init__(self,config_name):

        self.filename = os.path.join(setting.DATA_PATH,config_name)
        if os.path.exists(self.filename):
            self.file_name = self.filename
        else:
            raise FileNotFoundError('文件不存在')

    def load_yaml(self):
        '''
        读取yaml文件
        :param filename:
        :return:
        '''
        try:
            with open(self.file_name,'rb+') as f:
                content = yaml.safe_load(f)
                logger.info("Had read file info")
                return content
        except Exception as e:
            logger.error(e)

    def load_ini(self):
        '''
        读取ini文件
        :return:
        '''

        try:
            config = ConfigParser()
            config.read(self.file_name,encoding='utf-8')
            return config.get
        except Exception as e:
            logger.error(e)


class WriteFileData(object):
    '''
    写配置文件
    '''

    def __init__(self,config_name,content):
        self.file_name = os.path.join(setting.DATA_PATH,config_name)
        self.content = content


    def write_yaml(self):
        '''
        写yaml文件
        :param filename:
        :param content:
        :return:
        '''
        try:
            with open(r'%s'% self.file_name,'w') as f:
                yaml.dump(self.content,self.file_name)
                f.close()
        except Exception as e:
            logger.error(e)






if __name__ == '__main__':
    pass

