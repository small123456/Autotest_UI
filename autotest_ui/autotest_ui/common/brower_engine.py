import sys
import time

from selenium import  webdriver
from config import setting
from selenium.common.exceptions import WebDriverException
import platform
import os
from common.logger import Logger
import functools
import requests

logger = Logger('brower_engine').getLog()

chromedriver = os.path.join(setting.TOOLS_PATH,'chromedriver_1')
class WebInit:

    def __init__(self):
        self.browser = setting.BROWER.lower()
        self.baseurl = setting.CONSOLE_URL

    def inspect_url(self,url):

        rq = requests.get(url,timeout=setting.TIMEOUT)
        code = rq.status_code

        if code == 200:
            return True
        else:
            logger.error("%s地址请求不到" % self.baseurl)
            return False

    @property
    def url(self):
        return self.baseurl


    @url.setter
    def url(self,value):
        self.baseurl = value

    @property
    def firefox_args(self):
        '''
        火狐浏览器参数
        :return:
        '''
        opt = webdriver.FirefoxOptions()
        opt.add_argument('--no-sandbox')
        opt.add_argument('--disable-gpu')
        return opt

    @property
    def chrome_args(self):
        '''
        谷歌浏览器参数
        :return:
        '''
        opt = webdriver.ChromeOptions()
        opt.add_argument('--no-sandbox')
        opt.add_argument('--disable-gpu')
        return opt


    def browser_setup_args(self,driver):
        '''
        最大化
        :param driver:
        :return:
        '''

        #driver.maximize.window()
        driver.get(self.url)
        return driver

    @property
    def enable(self):
        return self.setup()


    def setup(self):
        '''
        开启驱动
        :return:
        '''
        try:
            if self.inspect_url(self.url):
                cur_sys = sys.platform.lower()

                if cur_sys == 'darwin':
                    if self.browser == 'chrome':
                        option = self.chrome_args
                        driver = webdriver.Chrome(chromedriver,options=option)
                        return self.browser_setup_args(driver)
                    elif self.browser == 'firefox':
                        option = self.chrome_args
                        driver = webdriver.Chrome(chromedriver, options=option)
                        return self.browser_setup_args(driver)
                    else:
                        logger.error(f'mac系统不支持此浏览器: {self.browser}')
                        return False
                elif cur_sys == 'linux':
                    if self.browser == 'chrome':
                        option = self.chrome_args
                        driver = webdriver.Chrome(chromedriver, options=option)
                        return self.browser_setup_args(driver)
                    elif self.browser == 'firefox':
                        option = self.chrome_args
                        driver = webdriver.Chrome(chromedriver, options=option)
                        return self.browser_setup_args(driver)
                    else:
                        logger.error(f'linux 系统不支持此浏览器: {self.browser}')
                        return False
                elif cur_sys == 'windows':
                    if self.browser == 'chrome':
                        option = self.chrome_args
                        driver = webdriver.Chrome(chromedriver, options=option)
                        return self.browser_setup_args(driver)
                    elif self.browser == 'firefox':
                        option = self.chrome_args
                        driver = webdriver.Chrome(chromedriver, options=option)
                        return self.browser_setup_args(driver)
                    else:

                        logger.error(f'windows 系统不支持此浏览器: {self.browser}')
                        return False
            else:
                logger.error("url 打不开")
                return False
        except Exception as e:
            logger.error(e)
            return False





if __name__ == '__main__':


     pass