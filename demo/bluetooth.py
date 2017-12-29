#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:kk


import bluetooth

neayby_devices = bluetooth.discover_devices(lookup_names=True)
print('found %d devices ' % len(neayby_devices))

for addr, name in neayby_devices:
    print(' %s  -   %s' % (addr, name))
