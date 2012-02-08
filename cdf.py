#!/usr/bin/python

import sys


data = map(lambda s: float(s.strip()), sys.stdin)

data.sort()

length = len(data)

for v,i in zip(data,range(len(data))):
    print v, i/float(length)

