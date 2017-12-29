#!/usr/bin/env python
# -*- coding:utf-8 -*- 

# 爬取新浪网站 新闻数据 保存结果到Excel表格

import requests
import pandas
import json
from time import ctime

result = {}
temp = []
data = []

url = "http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_=1513303426924"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "Referer": "http://news.sina.com.cn/china/"
}


def getHtml(url):
    try:
        res = requests.get(url, headers=headers, timeout=3)
    except Exception as e:
        print(e)
    return res.text


def parseData(res):
    global result
    jd = json.loads(res.lstrip('  newsloadercallback(').rstrip(');'))
    news = jd['result']['data']
    for news in news:
        result['id'] = news['id']
        result['create_time'] = news['createtime']
        result['create_time'] = ctime(int(result['create_time']))
        result['title'] = news['title']
        result['url'] = news['url']
        result['keywords'] = news['keywords']
        result['level'] = news['level']
        result['old_level'] = news['old_level']
        result['原标题'] = str(news['ext5']).lstrip('原标题：')
        result['media_name'] = news['media_name']
        temp.append(result)
        result = {}
    return result


def save(tempTosave):
    df = pandas.DataFrame(temp)
    df.to_excel('news.xlsx')


if __name__ == '__main__':
    for page in range(1, 200):
        print('processing --->page' + str(page))
        url2 = url.format(page)
        try:
            res = getHtml(url2)
        except Exception as e:
            print(e)
            continue
        parseData(res)
    save(temp)
    print(len(temp))
