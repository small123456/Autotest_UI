import pytest
from common.brower_engine import WebInit
from common.logger import Logger
import allure

logger = Logger('contest').getLog()
@allure.description("打开浏览器")
@pytest.fixture(scope="session")
def open_browswr():
    logger.info("执行fixture")
    wb = WebInit()
    driver = wb.enable
    yield driver

    logger.info("执行fixture")



