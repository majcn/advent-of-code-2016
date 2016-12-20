import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]


blocked = [map(int, d.split('-')) for d in data]

def isAllowed(i):
    for bl, bh in blocked:
        if i >= bl and i <= bh:
            return (False, bh)
    return (True, i)

result = [0, 0]
i = 0
while i <= 4294967295:
    allowed, i = isAllowed(i)
    if allowed:
        if result[0] == 0:
            result[0] = i
        result[1] += 1
    i += 1

print result
