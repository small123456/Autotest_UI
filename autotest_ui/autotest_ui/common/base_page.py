import os
import time

from common.page_action import find_element

from config import setting
from common import page_action
from common.logger import Logger
import pytest
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
logger = Logger('base_page').getLog()
class BasePage(object):

    def __init__(self,driver):

        self.driver = driver

    @property
    def get_title(self):
        '''
        获取title
        :return:
        '''
        return self.driver.title

    @property
    def get_url(self):
        '''
        获取当前url
        :return:
        '''
        return self.driver.current_url

    def get_attribute(self,name):
        '''
        获取属性值
        :param name:
        :return:
        '''
        element = self.find_element(selector)
        try:
            value = element.get_attribute(name)
            return value

        except Exception as e:
            logger.error(f"Fail to get attribute:{e}")




    def refersh(self):
        '''
        刷新页面
        :return:
        '''
        return self.driver.refersh()

    def back(self):
        '''
        返回上一级页面
        :return:
        '''
        return self.driver.back()

    def forward(self):
        '''
        继续一个页面
        :return:
        '''
        return self.driver.forward()

    def current_window(self):
        '''
        获取当前窗口句柄
        :return:
        '''

        current_window_handle = self.driver.current_window_handle
        return current_window_handle

    def all_window(self):
        '''
        获取当前所有窗口句柄
        :return:
        '''
        handles = self.driver.window_handles
        return handles

    def switch_window(self,index):
        '''
        多窗口切换
        :param index:
        :return:
        '''

        handle = self.all_window()[index]

        try:
            self.driver.switch_to.window(handle)
        except NoSuchWindowException as e:
            logger.error(f'切换到{e}失败')


    def find_element(self,selector):
        '''
        可见不可见元素定位
        :param selector:
        :return:
        '''

        return page_action.find_element(self.driver,selector)

    def find_element_by_content(self,selector,content):
        '''
        通过文本内容定位可见或者不可见元素
        :param selector:
        :param content:
        :return:
        '''

        return page_action.find_element(self.driver,selector,content=content)

    def find_element_by_visiable(self,selector):
        '''
        可见元素定位
        :param selector:
        :return:
        '''
        return page_action.find_element(self.driver,selector,state='visiable')

    def find_element_by_clickable(self,selector):
        '''
        可点击元素定位
        :param selector:
        :return:
        '''
        return page_action.find_element(self.driver,selector,state='clickable')

    def isElementEnabled(self,selector):
        '''
        判断元素是否可用
        :param selector:
        :return:
        '''
        return page_action.find_element(self.driver, selector, state='visiable').is_enabled()

    def isElementSelected(self,selector):
        '''
        判断元素是否可选
        :param selector:
        :return:
        '''
        return page_action.find_element(self.driver,selector,state='visiable').is_selected()

    def is_element_visiable(self,selector):
        '''
        判断元素是否可见
        :param selector:
        :return:
        '''
        if self.find_element_by_visiable(selector):
            return True
        else:
            return False

    def input(self,selector,value):
        '''
        文本框输入
        :param selector:
        :param value:
        :return:
        '''
        element = self.find_element(selector)
        print(element)
        try:
            element.send_keys(value)
        except Exception as e:
            logger.error(f"输入失败{e}")


    def ensure_click(self,selector):
        '''
        点击
        :param selector:
        :return:
        '''
        element = self.find_element_by_clickable(selector)

        self.scrollToElement(element)
        return page_action.smart_click(element)


    def ensure_click_content(self,selector,content):
        '''
        点击
        :param selector:
        :param content:
        :return:
        '''
        element = self.find_element_by_content(selector,content=content)
        self.scrollToElement(element)
        return page_action.smart_click(element)



    def clear(self,selector):
        '''
        清除
        :param selector:
        :return:
        '''

        element = self.find_element(selector)
        try:
            self.driver.execute_script('arguments[0].value=""',element)
            logger.info("清除成功")
        except Exception as e:
            logger.error(f"清除失败->{e}")



    def save_screen(self):
        '''
        截图
        :return:
        '''
        rq = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        filename = os.path.join(setting.SCREEN_PATH,self.get_title+rq+'.png')
        try:
            self.driver.save_screenshot(filename)
        except Exception as e:
            logger.error(e)



    def scrollToBottom(self):
        '''
        滚动到窗口底部
        :param selector:
        :return:
        '''
        try:
            self.driver.execute_script('window.scollTo(0,document.body.scrollHeight) ')
        except Exception as e:
            logger.error(e)

    def scrollToElement(self,element):
        '''
        滚动到元素位置
        :param element:
        :return:
        '''

        try:
            self.driver.execute_script('arguments[0].scrollIntoView()',element)
        except Exception as e:
            logger.error(e)


    def mark_color(self,selector):
        '''
        高亮
        :param selector:
        :return:
        '''

        element = self.find_element(selector)
        try:
            self.driver.execute_script('arguments[0].setAttribute("style",arguments[1]);',element,'border: 2px solid red;')
            logger.info("标红成功")
        except Exception as e:
            logger.error(e)
            raise (e)

    def accept(self):
        '''
        警告框确认
        :return:
        '''
        try:
            self.driver.switch_to.alert().accept()
            logger.info("警告框已经确认")
        except Exception as e:
            logger.error(f'查找alert弹出框异常->{e}')

    def dismiss(self):
        '''
        警告框取消
        :return:
        '''
        try:
            self.driver.switch_to.alert().dismiss()
            logger.info("警告框已经确认")
        except Exception as e:
            logger.error(f'查找alert弹出框异常->{e}')


    def keyEnter(self,selector):
        '''
        按回车键
        :return:
        '''
        element = self.find_element(selector)
        try:
            element.send_keys(Keys.ENTER)
        except Exception as e:
            logger.error(f"回车按键失败-> {e}")


    def ctrl_a(self):
        '''
        全选
        :return:
        '''

        try:
            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
            logger.info("ctrl_a successful")
        except Exception as e:
            logger.error(f"ctrl_a fail -> {e}")

    def ctrl_c(self):
        '''
        复制
        :return:
        '''
        try:
            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
            logger.info("ctrl_a successful")
        except Exception as e:
            logger.error(f"ctrl_a fail -> {e}")

    def ctrl_v(self,selector):
        '''
        粘贴
        :param selector:
        :return:
        '''
        element = self.find_element(selector)
        try:
            ActionChains(self.driver).key_down(Keys.CONTROL,element).send_keys('v').key_up(Keys.CONTROL).perform()
            logger.info("ctrl_a successful")
        except Exception as e:
            logger.error(f"ctrl_a fail -> {e}")

    def drag_and_drop(self,selector_start,selector_target):
        '''
        拖拽
        :param selector_start:
        :param selector_target:
        :return:
        '''
        element_start = self.find_element(selector_start)
        element_target = self.find_element(selector_target)

        try:
            ActionChains(self.driver).drag_and_drop(element_start,element_target).perform()
        except Exception as e:
            logger.error(f"拖拽失败->{e}")



    def element_havor(self,selector):
        '''
        鼠标悬停
        :param selector:
        :return:
        '''

        element = self.find_element(selector)
        try:
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception as e:
            logger.error(f'鼠标悬停位置{selector}失败')

    def element_havor_click(self,selector):
        '''
        鼠标悬停点击
        :param selector:
        :return:
        '''
        element = self.find_element(selector)
        try:
            ActionChains(self.driver).move_to_element(element).click().perform()
        except Exception as e:
            logger.error(f'鼠标悬停位置失败->{e}')

    def select_element(self,selector,value):
        '''
        选中框
        :param selector:
        :param value:
        :return:
        '''

        element = self.find_element(selector)
        if not self.isElementSelected(selector):

            return element.select_by_value(value)

        else:
            logger.info("已选中")














