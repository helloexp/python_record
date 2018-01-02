#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 可用
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '120861745@qq.com'  # 发件人邮箱账号
my_pass = 'xcwnwcapsewacabi'  # 发件人邮箱密码   备用    sawlgkaktiwobigh
receiver = 'wangzqdd@163.com'  # 收件人邮箱账号


def mail(content='填写邮件内容',id=34):
    flag = True
    try:
        msg = MIMEText(content, 'plain', 'utf-8')     # 在这里输入正文
        msg['From'] = formataddr(["档案处", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "绝密文档"+str(id)  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [receiver, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(str(e))
        flag = False
    return flag


if __name__ == '__main__':
    ret = mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
