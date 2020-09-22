# from smtplib import SMTP_SSL
# from email.mime.text import MIMEText
# from email.header import Header
#
# email_from = "1152475833@qq.com"  # 改为自己的发送邮箱
# email_to = "972059909@qq.com"  # 接收邮箱
# hostname = "smtp.qq.com"  # 不变，QQ邮箱的smtp服务器地址
# login = "1152475833@qq.com"  # 发送邮箱的用户名
# password = "eikhfsjbjiihgfbh"  # 发送邮箱的密码，即开启smtp服务得到的授权码。注：不是QQ密码。
# subject = "python+smtp"  # 邮件主题
# text = "send email"  # 邮件正文内容
#
# smtp = SMTP_SSL(hostname)  # SMTP_SSL默认使用465端口
# smtp.login(login, password)
#
# msg = MIMEText(text, "plain", "utf-8")
# msg["Subject"] = Header(subject, "utf-8")
# msg["from"] = email_from
# msg["to"] = email_to
#
# smtp.sendmail(email_from, email_to, msg.as_string())
# smtp.quit()
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = '1152475833@qq.com'
    receivers = ['972059909@qq.com']
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = Header('王大锤', 'utf-8')
    message['To'] = Header('骆昊', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.qq.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'eikhfsjbjiihgfbh')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()