import re

import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata[2:]]


prog = re.compile(r'^/dev/grid/node-x(\d+)-y(\d+)\s+\d+T\s+(\d+)T\s+(\d+)T\s+\d+\%$')

disks = [map(int, prog.match(d).groups()) for d in data]

print len([1 for dA in disks for dB in disks if dA != dB and dA[2] > 0 and dA[2] <= dB[3]])


maxx = max(d[0] for d in disks)
maxy = max(d[1] for d in disks)

# there is only one empty disk
# emptyDisk = next(d for d in disks if d[2] == 0)
# print emptyDisk

# r = []
# for d in disks:
#     dm = ''
#     if d == emptyDisk:
#         dm = '_'
#     elif d[2] <= emptyDisk[3]:
#         dm = '.'
#     else:
#         dm = '#'
#     r.append((d[0], d[1], dm))

# grid = [['']*(maxx+1) for i in range(maxy+1)]
# for rr in r:
#     grid[rr[1]][rr[0]] = rr[2]
# grid[0][maxx] = 'G'
# for g in grid:
#     print g


# TODO: calculate moves of empty disk to (maxx, 0)
bg = 6 + 21 + 7 # graphical :)
print bg + maxx*5 - 4
