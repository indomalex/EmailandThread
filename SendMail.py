#coding:utf-8

import smtplib


#发送一封邮件到我的QQ邮箱
from email.header import Header
from email.mime.text import MIMEText


def sendMail():
    try:
        subject = "这是从python发来的测试邮件"
        txt = "用python从QQ邮箱发来的邮件，OK"
        fromAddr = "kerry.xia@qq.com"
        toAddr = "13594387943@139.com"
        smtpServer = "smtp.qq.com"
        username = "kerry.xia@qq.com"
        pwd = "vrnzfngqnmembhca"

        msg = MIMEText(txt, 'plain', 'utf-8')
        # msg['Subject'] = Header(subject, 'utf-8')
        msg['Subject'] = subject
        #下边两个不写的话有可能看不到发件人
        msg["From"] = fromAddr
        msg["To"] = toAddr

        smtp = smtplib.SMTP_SSL(smtpServer, 465)
        smtp.login(username, pwd)
        smtp.sendmail(fromAddr, toAddr, msg.as_string())
        smtp.quit()
        print("邮件已成功发送。")
    # except BaseException as e:
    except smtplib.SMTPException as e:
        print("邮件发送失败:" + str(e))


if __name__ == "__main__":
    sendMail()
