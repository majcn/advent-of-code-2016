import sys
inputdata = sys.stdin.readline()

data = [x.strip() for x in inputdata.split(",")]
data = [(x[0], int(x[1:])) for x in data]


# 0 -> up; 1 -> right; 2 -> down; 3 -> left
moveDict = {
    0: lambda x, y: (x, y + 1),
    1: lambda x, y: (x + 1, y),
    2: lambda x, y: (x, y - 1),
    3: lambda x, y: (x - 1, y)
}

directions = {
    0: { 'L': 3, 'R': 1},
    1: { 'L': 0, 'R': 2},
    2: { 'L': 1, 'R': 3},
    3: { 'L': 2, 'R': 0},
}

locations = [(0, 0)]
direction = 0
for d, l in data:
    direction = directions[direction][d]
    for i in range(l):
        locations.append(moveDict[direction](*locations[-1]))

def getVisitTwice(locations):
    for i1, l1 in enumerate(locations):
        for i2, l2 in enumerate(locations):
            if (i1 != i2 and l1 == l2):
                return l1
    return None

def getLocationLength(location):
    return abs(location[0]) + abs(location[1])

print getLocationLength(locations[-1])
print getLocationLength(getVisitTwice(locations))