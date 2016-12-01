import sys
inputdata = sys.stdin.readline()

data = [x.strip() for x in inputdata.split(",")]
data = [(x[0], int(x[1:])) for x in data]


# 0 -> up; 1 -> right; 2 -> down; 3 -> left
move = {
    0: lambda x, y: (x, y + 1),
    1: lambda x, y: (x + 1, y),
    2: lambda x, y: (x, y - 1),
    3: lambda x, y: (x - 1, y)
}

nextDirection = {
    0: { 'L': 3, 'R': 1},
    1: { 'L': 0, 'R': 2},
    2: { 'L': 1, 'R': 3},
    3: { 'L': 2, 'R': 0},
}

locations = [(0, 0)]
direction = 0
for d, l in data:
    direction = nextDirection[direction][d]
    for i in range(l):
        locations.append(move[direction](*locations[-1]))

result = [
    locations[-1],
    next(l for i, l in enumerate(locations) if l in locations[(i+1):])
]
print map(lambda x: abs(x[0]) + abs(x[1]), result)
