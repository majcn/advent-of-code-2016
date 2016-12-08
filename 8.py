from collections import deque
import re

import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]


def fill(a, b):
    global result

    for i in range(a):
        for j in range(b):
            result[j][i] = 1

def rotateX(c, v):
    global result

    transpose_t = zip(*result)
    tmp = deque(transpose_t[c])
    tmp.rotate(v)
    transpose_t[c] = tmp

    result = map(list, zip(*transpose_t))

def rotateY(c, v):
    global result

    tmp = deque(result[c])
    tmp.rotate(v)
    result[c] = list(tmp)

commands = [
    (re.compile(r'^rect ([0-9]*)x([0-9]*)$'),               fill),
    (re.compile(r'^rotate column x=([0-9]*) by ([0-9]*)$'), rotateX),
    (re.compile(r'^rotate row y=([0-9]*) by ([0-9]*)$'),    rotateY)
]

result = [[0]*50 for x in range(6)]
[[m[1](*map(int, m[0].groups())) for m in [next(command for command in map(lambda x: (x[0].match(d), x[1]), commands) if command[0] != None)]] for d in data]

print sum(map(sum, result))
print '\n'.join(''.join('#' if item == 1 else ' ' for item in row) for row in result)
