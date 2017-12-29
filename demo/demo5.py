#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:kk

def power(x):
    return x*x

def power2(x,n=2):
    sum=1
    while n>0:
        n=n-1
        sum=sum*x
    return sum

def enroll(name,gender,age=6,city='BJ'):
    print(name,gender,age,city)

def calc(*num):
    s=0
    for i in num:
        s=s+i*i
    return s

print(power(5))
print(power2(5,3))
enroll('Tom','male',8)
print(calc(3,4))