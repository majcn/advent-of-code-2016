import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]
data = [map(int, x.split()) for x in data]

data2 = map(list, zip(*[iter([d[i] for i in range(3) for d in data])]*3))

def isValidTriange(t):
    i, v = max(enumerate(t), key=lambda x: x[1])
    return sum(t[:i] + t[(i+1):]) > v

print map(lambda d: len(filter(isValidTriange, d)), [data, data2])