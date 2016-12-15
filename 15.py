import re

import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]
prog = re.compile(r'^Disc #\d* has (\d*) positions; at time=0, it is at position (\d*)\.$')
INPUT = [tuple(map(int, prog.match(d).groups())) for d in data]

print [next(time for time in xrange(sys.maxint) if all((ci[i][1] + i + time + 1) % ci[i][0] == 0 for i in range(len(ci)))) for ci in [INPUT, INPUT + [(11, 0)]]]
