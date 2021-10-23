import sys

import pytest
import allure
from common.logger import Logger
from common.base_page import BasePage
from pagemodels.delete_vm import DeleteVM
from common.file_process import ReadFileData

#skipmark = pytest.mark.skipif(sys.platform !='linux',reason="tigao")
#@pytest.mark.dependency(depends=['TestCreateVM'])
@allure.severity("normal")
@allure.epic("test5")
@pytest.mark.deletevm
@pytest.mark.run(order=2)
class TestDeleteVM():

    @allure.issue("http://www.baidu.com",name='bug')
    def test_ClearVM(self,open_browswr):
        """
        删除vm
        :param open_browswr:
        :return:
        """

        delete = DeleteVM(open_browswr)


        delete.clear_username()

        delete.clear_password()

        delete.save_screen()

