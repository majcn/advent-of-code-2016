import re

import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata[2:]]


prog = re.compile(r'^/dev/grid/node-x(\d+)-y(\d+)\s+\d+T\s+(\d+)T\s+(\d+)T\s+\d+\%$')

disks = [map(int, prog.match(d).groups()) for d in data]

print len([1 for dA in disks for dB in disks if dA != dB and dA[2] > 0 and dA[2] <= dB[3]])
