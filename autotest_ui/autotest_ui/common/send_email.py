# -*- coding: UTF-8 -*-
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from config import setting
from logger import Logger

logger = Logger('send_email').getLog()

def SendMail(file_name):
    '''
    邮件发送
    :param file_name:
    :return:
    '''

    filename = os.path.join(setting.REPORT_PATH,'%s' % file_name)
    with open(filename,'rb+') as f:
        report = f.read()

    # 邮件首部
    message = MIMEMultipart()
    message['From'] = setting.FROM_ADDR
    message['To'] = setting.TO_ADDR
    subject = '自动化测试报告'
    message['Subject'] = Header(subject,'utf-8')


    #正文内容
    message.attach(MIMEText('自动化测试报告在附件，请查收','plain','utf-8'))

    #添加附件
    att = MIMEText(report,'plain','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    # 邮件附件的名字
    att["Content-Disposition"] = 'attachment; filename=%s' % filename
    message.attach(att)

    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect("smtp.163.com", "25")
        state = smtp_obj.login(setting.FROM_ADDR, setting.PASSWORD)
        if state[0] == 235:
            smtp_obj.sendmail(setting.FROM_ADDR, setting.TO_ADDR, message.as_string())
            logger.info("Sent mail successfully!")
        smtp_obj.quit()
    except smtplib.SMTPException as e:
        logger.error(str(e))









if __name__ == '__main__':
    SendMail('report')




