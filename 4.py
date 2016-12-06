from collections import Counter
import re

import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

prog = re.compile(r'^([a-z,\-]*)([0-9]*)\[([a-z]*)\]$')

def ceasar(story, shift):
    return ''.join(('abcdefghijklmnopqrstuvwxyz'*2)[ord(char) - ord('a') + shift % 26] if char.isalpha() else char for char in story)

result = 0
for d in data:
    m = prog.match(d)
    x,y,z = m.group(1), int(m.group(2)), m.group(3)
    if sorted(map(lambda ii: ii[0], sorted(Counter(x.replace('-', '')).iteritems(), key=lambda i: (1./i[1], i[0]))[:len(z)])) == sorted(list(z)):
        result += y
    if 'northpole-object-storage-' == ceasar(x, y):
        print 'North Pole objects are stored: ' + str(y)
print result
