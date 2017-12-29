#!/usr/bin/env python
# -*- coding:utf-8 -*- 

# 下载豆瓣电影的图片

import requests
from bs4 import BeautifulSoup
import re
import os


def getHtml(url):
    links = []
    names = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Referer": "https://movie.douban.com/"
    }

    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')

    img = soup.find_all('img')
    for i in img:
        # print(i)
        link = i['src']
        if re.search(r'alt', str(i)):
            name = i['alt']
        if str(link).endswith("jpg"):
            links.append(str(link))
            names.append(str(name))
    print(links)
    print(names)
    index = 0
    for link in links:
        print(link)
        if re.search('wechat',link):
            continue
        res = requests.get(link)
        if res.status_code == 200:
            if not os.path.exists('./images/'):
                os.makedirs('./images/')
            for i in '\\/:*?"<>|':
                if i in names[index]:
                    names[index]=str(names[index]).replace(i,'_A_')

            f2= open('./images/'+names[index] + '.jpg', 'wb')
            print('downloading-->' + names[index])
            f2.write(res.content)
            f2.close()
            index += 1


if __name__ == "__main__":
    url = "https://movie.douban.com/"
    getHtml(url)
