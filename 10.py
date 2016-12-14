from collections import defaultdict
import re

import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

prog_init = re.compile(r'^value (\d*) goes to bot (\d*)$')
prog_move = re.compile(r'^bot (\d*) gives low to (bot|output) (\d*) and high to (bot|output) (\d*)$')

commands = {}
bots = defaultdict(list)
output = defaultdict(list)
for d in data:
    m = prog_init.match(d)
    if m:
        v, b = map(int, m.groups())
        bots[b].append(v)

    m = prog_move.match(d)
    if m:
        b, ll, lv, hl, hv = m.groups()
        b, lv, hv = map(int, [b, lv, hv])
        commands[b] = (ll, lv, hl, hv)


responsible = None
def goToBots():
    global responsible
    global bots
    global output

    for bot in bots:
        if len(bots[bot]) == 2:
            vl, vh = sorted(bots[bot])
            if vl == 17 and vh == 61:
                responsible = bot
            bots[bot] = []
            ll, lv, hl, hv = commands[bot]
            if ll == 'output':
                output[lv].append(vl)
            else:
                bots[lv].append(vl)

            if hl == 'output':
                output[hv].append(vh)
            else:
                bots[hv].append(vh)
            return True
    return False

while True:
    if not goToBots():
        break

print responsible
print reduce(lambda r,x: r*x, map(lambda v: output[v][0], [0,1,2]))
