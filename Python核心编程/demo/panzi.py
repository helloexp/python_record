#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:kk


# 解决汉诺塔问题
def move(n,a,b,c):
    global count
    if n==1:
        count+=1
        print('move',a,'->',c)

    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

if __name__=='__main__':
    count=0
    move(4,'A','B','C')
    print(count)