#!/usr/bin/env python
# -*- coding:utf-8 -*- 

# 版本v1.0

from bs4 import BeautifulSoup
import requests
import re
import time
import mail


def getHtml(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Referer": "https://www.baidu.com/link?url=4JvPElSs3Gw3FoU72P3CU5lt-XBP1m5_m_BDcsyUntsRJzNcqVGn8jwC82nLUced&wd=&eqid=fbff25c000001ee4000000025a4ae0d0"
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    return soup


def getContent(soup):
    links = []
    title = soup.select('dd')
    for i in title:
        title_num = i.select('a')[-1].text
        flag = re.search('\d{1,4}', title_num).group()
        print(flag)
        title_num = flag
        title = i.select('a')[-1].text
        link = i.select('a')[-1]['href']
        links.append(title_num + "==" + title + "==" + "https://www.xxbiquge.com" + link)
    f = open('./max_num', 'w')
    title_num=int(title_num)+1
    f.write(str(title_num))
    f.close()
    return links


def getNovel(num, links):
    for link in links:
        if str(num) in link:
            a = link.split('==')[-1]
            title = link.split('==')[-2]
            soup2 = getHtml(a)
            content = soup2.select('#content')[0].text.replace('<br>', " ").strip().lstrip('纯文字在线阅读本站域名手机同步阅读请访问')
    return title, content


def main():
    f2=open('./max_read','r')
    init = int(f2.read())
    f2.close()
    f2 = open('./max_read', 'w')
    url = "https://www.xxbiquge.com/9_9511/"
    soup = getHtml(url)
    links = getContent(soup)
    f = open('./max_num', 'r')
    for i in f:
        while init < int(i):
            title, content = getNovel(init, links)
            print(title, content)
            article = ' 密级：绝密   使用人员：专人专用   授权人员：S2   使命：I#  ++++++++ ' + title + " ++++++++  " + time.asctime(
                time.localtime(time.time())) + "------->" + content
            ret = mail.mail(article, init)
            if ret:
                print("邮件发送成功", init)
            else:
                print("邮件发送失败")
                continue
            init += 1
    f2.write(str(init-1))
    f2.close()

if __name__ == "__main__":
    main()
    record = open('./record.txt', 'a')
    record.write(str(time.asctime(time.localtime(time.time()))) + '-->  success\n')
    record.close()

