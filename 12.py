import re

import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

cpy = re.compile(r'^cpy (-?\d*|[abcd]) ([abcd])$')
inc = re.compile(r'^inc ([abcd])$')
dec = re.compile(r'^dec ([abcd])$')
jnz = re.compile(r'^jnz (\d*|[abcd]) (-?\d*)$')
def getRegexResult(prog, s):
    m = prog.match(s)
    return m.groups() if m else []

def handleCpy(r, x, y):
    if x.isalpha():
        xv = r[1][x]
    else:
        xv = int(x)

    r[1][y] = xv

def handleInc(r, x):
    r[1][x] += 1

def handleDec(r, x):
    r[1][x] -= 1

def handleJnz(r, x, y):
    if x.isalpha():
        xv = r[1][x]
    else:
        xv = int(x)

    if xv != 0:
        r[0] += (int(y) - 1)

commands = []
for d in data:
    rc = (getRegexResult(cpy, d), handleCpy)
    ri = (getRegexResult(inc, d), handleInc)
    rd = (getRegexResult(dec, d), handleDec)
    rj = (getRegexResult(jnz, d), handleJnz)

    commands.append(filter(lambda x: x[0], [rc, ri, rd, rj])[0])

r = [0, {'a': 0, 'b': 0, 'c': 0, 'd': 0}] # for part 1 -> 'c': 0
while r[0] < len(commands):
    cmd = commands[r[0]]
    cmd[1](r, *cmd[0])
    r[0] += 1

print r