import re

import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]


def getRegexResult(prog, s):
    m = prog.match(s)
    return m.groups() if m else []

def handle_sp(s, x, y):
    x = int(x)
    y = int(y)

    lresult = list(s)
    tmp = lresult[x]
    lresult[x] = lresult[y]
    lresult[y] = tmp

    return ''.join(lresult)

def handle_sl(s, x, y):
    return s.replace(x, '$').replace(y, x).replace('$', y)

def handle_rl(s, x):
    x = int(x)

    return s[x:] + s[:x]

def handle_rr(s, x):
    x = int(x)

    return s[-x:] + s[:-x]

def handle_rp(s, x):
    i = s.index(x)

    r = handle_rr(s, 1)
    r = handle_rr(r, i)
    if i >= 4:
        r = handle_rr(r, 1)

    return r

def handle_rv(s, x, y):
    x = int(x)
    y = int(y)

    return s[:x] + s[x:(y+1)][::-1] + s[(y+1):]

def handle_mv(s, x, y):
    x = int(x)
    y = int(y)

    lresult = list(s)
    tmp = lresult[x]
    del lresult[x]
    lresult.insert(y, tmp)

    return ''.join(lresult)

rules = [
    (re.compile(r'^swap position (\d*) with position (\d*)$'), handle_sp),
    (re.compile(r'^swap letter (\w) with letter (\w)$'), handle_sl),
    (re.compile(r'^rotate left (\d*) steps?$'), handle_rl),
    (re.compile(r'^rotate right (\d*) steps?$'), handle_rr),
    (re.compile(r'^rotate based on position of letter (\w)$'), handle_rp),
    (re.compile(r'^reverse positions (\d*) through (\d*)$'), handle_rv),
    (re.compile(r'^move position (\d*) to position (\d*)$'), handle_mv)
]

def run(input):
    global data

    r = input
    for d in data:
        params, handler = filter(lambda x: x[0], [(getRegexResult(prog, d), handler) for prog, handler in rules])[0]
        r = handler(r, *params)
    return r

# part 1
print run('abcdefgh')

# ugly part 2
from itertools import permutations
print next(''.join(p) for p in permutations('abcdefgh') if run(''.join(p)) == 'fbgdceah')
