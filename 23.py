import re

import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

cpy = re.compile(r'^cpy (-?\d*|[abcd]) ([abcd])$')
inc = re.compile(r'^inc ([abcd])$')
dec = re.compile(r'^dec ([abcd])$')
jnz = re.compile(r'^jnz (-?\d*|[abcd]) (-?\d*|[abcd])$')
tgl = re.compile(r'^tgl (-?\d*|[abcd])$')
def getRegexResult(prog, s):
    m = prog.match(s)
    return m.groups() if m else []

def readValue(r, x):
    return r[1][x] if x.isalpha() else int(x)

def handleCpy(r, commands, x, y):
    xv = readValue(r, x)
    r[1][y] = xv

def handleInc(r, commands, x):
    r[1][x] += 1

def handleDec(r, commands, x):
    r[1][x] -= 1

def handleJnz(r, commands, x, y):
    xv = readValue(r, x)
    yv = readValue(r, y)

    if xv != 0:
        r[0] += (yv - 1)

def handleTgl(r, commands, x):
    xv = readValue(r, x)

    l = r[0] + xv
    if l > 0 and l < len(commands):
        c = commands[l]
        c[1] = { handleCpy: handleJnz, handleInc: handleDec, handleDec: handleInc, handleJnz: handleCpy, handleTgl: handleInc }[c[1]]

def optimization(r, commands):
    # cpy b c
    # inc a
    # dec c
    # jnz c -2
    # dec d
    # jnz d -5

    if r[0] < len(commands) - 5:
        cmd0, cmd1, cmd2, cmd3, cmd4, cmd5 = commands[r[0]:r[0]+6]

        if cmd0[1] == handleCpy and cmd0[0] == ('b', 'c',) and cmd1[1] == handleInc and cmd1[0] == ('a',) and cmd2[1] == handleDec and cmd2[0] == ('c',) and cmd3[1] == handleJnz and cmd3[0] == ('c', '-2',) and cmd4[1] == handleDec and cmd4[0] == ('d',) and cmd5[1] == handleJnz and cmd5[0] == ('d', '-5',):
            r[1]['a'] += r[1]['b'] * r[1]['d']
            r[1]['c'] = 0
            r[1]['d'] = 0
            r[0] += 5

rules = [
    lambda d: [getRegexResult(cpy, d), handleCpy],
    lambda d: [getRegexResult(inc, d), handleInc],
    lambda d: [getRegexResult(dec, d), handleDec],
    lambda d: [getRegexResult(jnz, d), handleJnz],
    lambda d: [getRegexResult(tgl, d), handleTgl]
]

input = [7, 12]
for i in input:
    commands = map(lambda x: next(r(x) for r in rules if r(x)[0]), data)
    r = [0, {'a': i, 'b': 0, 'c': 0, 'd': 0}]

    while r[0] < len(commands):
        optimization(r, commands)

        cmd = commands[r[0]]
        cmd[1](r, commands, *cmd[0])
        r[0] += 1

    print '{:>2} eggs: {}'.format(i, r[1]['a'])
