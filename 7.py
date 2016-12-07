import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]


def flattenToSet(l):
    return set(item for sublist in l for item in sublist)

def prepareDataLine(d):
    outside = []
    inside = []
    s = ''
    for c in d:
        if c == '[':
            outside.append(s)
            s = ''
        elif c == ']':
            inside.append(s)
            s = ''
        else:
            s += c
    outside.append(s)

    return (outside, inside)

result = [0, 0]
for d in data:
    outside, inside = prepareDataLine(d)

    # bool -> int ( True = 1; False = 0 )
    result[0] += not any(any(j == j[::-1] and j[0] != j[1] for j in [x[i:i+4] for i in range(len(x) - 3)]) for x in inside) and \
                     any(any(j == j[::-1] and j[0] != j[1] for j in [x[i:i+4] for i in range(len(x) - 3)]) for x in outside)

    result[1] += bool(flattenToSet([[       j           for j in [x[i:i+3] for i in range(len(x) - 2)] if j == j[::-1]] for x in inside]) & \
                      flattenToSet([[j[1] + j[0] + j[1] for j in [x[i:i+3] for i in range(len(x) - 2)] if j == j[::-1]] for x in outside]))

print result