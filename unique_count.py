#!/usr/bin/python

import sys

d = {}
for l in sys.stdin:
    l = l.strip()
    d.setdefault(l,0)
    d[l] += 1

keys = d.keys()
keys.sort(cmp = lambda k1,k2: cmp(d[k1],d[k2]))
for k in keys:
    print ":".join(map(str,(k,d[k])))
