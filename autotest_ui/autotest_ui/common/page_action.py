from .logger import Logger
from config import setting
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

logger = Logger("page_action").getLog()


def find_element(driver,selector,state='presence',content=None,timeout=setting.TIMEOUT):

    find_by = (
        'id', 'name', 'xpath', 'link text', 'link_text', 'tag name', 'tag_name', 'class name', 'class_name',
        'css selector', 'css_selector', 'css')


    (selector_by,selector_value) = [selector.strip() for selector in selector.split('=>')]

    if selector_by not in find_by:
        logger.info("Selector_by {%s} is invalid!" % selector_by)
        raise NameError("Please enter a valid type of targeting elements.",selector_by)

    if selector_by == 'link_text':
        selector_by = 'link text'
    elif selector_by == 'tag_name':
        selector_by = 'tag name'
    elif selector_by == 'class_name':
        selector_by = 'class name'
    elif selector_by == 'css_selector':
        selector_by = 'css selector'

    if content:
        selector_value = selector_value.replace('%s',content)

    if state == 'presence':
        element = WebDriverWait(driver,timeout).until(
            EC.presence_of_element_located((selector_by,selector_value)),
            message='presence timeout %s=>%s' %(selector_by,selector_value)
        )
    elif state == 'visiable':
        element = WebDriverWait(driver,timeout).until(
            EC.visibility_of_element_located((selector_by,selector_value)),
            message='visiable timeout%s=>%s' %(selector_by,selector_value)
        )
    elif state == 'clickable':
        element = WebDriverWait(driver,timeout).until(
            EC.element_to_be_clickable((selector_by,selector_value)),
            message='clickable timeout %s=>%s'%(selector_by,selector_value)
        )

    return element


def smart_click(element):
    '''
    智能点击
    :return:
    '''
    start = time.time()
    end = start + setting.TIMEOUT

    while time.time() < end:
        try:
            element.click()
            return element
        except:
            time.sleep(1)

    logger.error("点击失败")


