#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:kk

# 计算n的阶乘


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


if __name__ == '__main__':
    print(fact(5))
