from collections import Counter

import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]


print [''.join([Counter([d[i] for d in data]).most_common()[j][0] for i in range(len(data[0]))]) for j in [0, -1]]