#!/usr/bin/env python
# -*- coding:utf-8 -*- 

url='http://www.baidu.com/?page={}'
for page in range(1,10):
    print(url.format(page))