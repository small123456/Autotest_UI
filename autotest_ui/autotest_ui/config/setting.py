
import os
import sys

ENV = 'test'
TIMEOUT = 10
BROWER = 'Chrome'
REMOTE_BROWER = 'Chrome'
REMOTE_URL = 'test'


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(BASE_PATH,'log')
REPORT_PATH = os.path.join(BASE_PATH,'report/report_dir')
DATA_PATH = os.path.join(BASE_PATH,'data')
TOOLS_PATH = os.path.join(BASE_PATH,'tool')
SCREEN_PATH = os.path.join(BASE_PATH,'screen')
TEMP_PATH = os.path.join(BASE_PATH,'report/temp_dir')
print(REPORT_PATH)


#邮件信息
SMTP_SERVER = 'smtp.163.com'
FROM_ADDR = '13571877753@163.com'
PASSWORD = 'RJWMBTFVYEWODGYH'
TO_ADDR = '1158392644@qq.com'


CONSOLE_URL = 'https://sso1.capitalonline.net/pages/login.html?next=http://console.capitalonline.net/vdc'

print(sys.platform.lower())
print(TOOLS_PATH)