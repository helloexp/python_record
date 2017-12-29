#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:kk

import tornado

name = "hello"
for i in range(10):
    print(i, end='')
    print(i, end='')
    # TODO 已经实现了打印不换行，接下来再实现其它功能
    print(i, end='')
print(name)
