import logging
import time
import os
from config import setting
import platform

class Logger():

    def __init__(self,name):

        # 创建logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)


        # 创建handler 用于写入文件
        rq = time.strftime("%Y-%m-%d %H",time.localtime(time.time()))
        log_filename = os.path.join(setting.LOG_PATH,'%s'% rq)
        fh = logging.FileHandler(log_filename,encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 创建handler 用于控制台输出
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)

        # 定义handler的输出格式

        formater = logging.Formatter('%(asctime)s-%(filename)s-%(levelname)s-%(message)s')
        fh.setFormatter(formater)
        sh.setFormatter(formater)

        self.logger.addHandler(fh)
        self.logger.addHandler(sh)

    def __call__(self, *args, **kwargs):
        return self.logger

    def getLog(self):
        return self.logger

if __name__ == '__main__':
    logger = Logger('setting').getLog()
    logger.info('test')
    print(platform.system())