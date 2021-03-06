import pytest
from config import setting
import os

report = setting.REPORT_PATH
temp = setting.TEMP_PATH
pytest.main(['-s','-v','--reruns=0','--alluredir',f'{temp}','--allure-epics=test3'])
os.system(f'allure generate {temp} -o {report} --clean')


