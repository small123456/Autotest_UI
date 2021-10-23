import allure
import pytest
from common.logger import Logger
from common.base_page import BasePage
from pagemodels.create_vm import CreateVM
from common.file_process import ReadFileData

logger = Logger('crestevm').getLog()

conf = ReadFileData('vm1.yaml').load_yaml()['login']
data = [(conf['username'],conf['password'])]
#skipmark = pytest.mark.skip(reason="不能运行")
#@allure.title("duogecanshu {username},{password}")
#@pytest.mark.dependency()
#@skipmark
#@pytest.mark.xfail
#@pytest.mark.createvm
#@pytest.mark.run(order=1)
#@pytest.mark.parametrize('username,password',data)
@allure.epic("test3")
@allure.feature("test2")
@allure.story("test1")
class TestCreateVM():
    @allure.severity("critical")
    @allure.link("http://www.baidu.com",name="cshi")
    @allure.title('创建')
    @allure.description("test")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('username,password', data)
    def test_CreateVM(self,open_browswr,username,password):

        create = CreateVM(open_browswr)


        create.input_username(username)

        create.input_password(password)

        create.save_screen()
        allure.dynamic.feature("xiugaizhog")
        allure.dynamic.story("dongtAI")

        allure.dynamic.title(f"xiugaibiaoti->{username},{password}")

        allure.dynamic.description("miaoshu")

        pytest.assume(1 == 1)






if __name__ == '__main__':
    pytest.main(['-s','-v'])