#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:kk

import math

def move(x, y, step=1):
    nx = x + step
    ny = y + step
    return nx, ny

def quadratic(a,b,c):
    #a*x*x+b*x+c=0
    fenzi_1=-b+math.sqrt(b*b-4*a*c)
    fenzi_2=-b-math.sqrt(b*b-4*a*c)
    fenmu=2*a
    x=fenzi_1/fenmu
    x=fenzi_2/fenmu
    return x,-x

if __name__=='__main__':
    x, y = move(10, 20, 3)
    print(x, y)
    x1,x2=quadratic(1,3,-4)
    print(x1,x2)
    print(math.sqrt(2))