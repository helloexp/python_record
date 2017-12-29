#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import requests
import pandas
import json

result = {}
temp = []
data = []

url = "http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_=1513303426924"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "Referer": "http://news.sina.com.cn/china/"
}
for page in range(1,30):
    url=url.format(page)
    try:
        res = requests.get(url, headers=headers, timeout=3)
    except Exception as e:
        print(e)
        continue
    print(str(page)+'-->',res.status_code)
    jd = json.loads(res.text.lstrip('  newsloadercallback(').rstrip(');'))
    news = jd['result']['data']

    for news in news:
        result['id'] = news['id']
        result['title'] = news['title']
        result['url'] = news['url']
        result['keywords'] = news['keywords']
        result['level'] = news['level']
        result['old_level'] = news['old_level']
        result['原标题'] = str(news['ext5']).lstrip('原标题：')
        result['media_name'] = news['media_name']

        temp.append(result)
        result={}
print(temp)

df = pandas.DataFrame(temp)
df.to_excel('news.xlsx')
