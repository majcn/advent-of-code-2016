import sys
inputdata = sys.stdin.readline()

data = [x.strip() for x in inputdata.split(",")]
data = [(x[0], int(x[1:])) for x in data]


UP, RIGHT, DOWN, LEFT = (0,1,2,3)

move = {
    UP:    lambda loc, d: (loc[0]    , loc[1] + d),
    RIGHT: lambda loc, d: (loc[0] + d, loc[1]    ),
    DOWN:  lambda loc, d: (loc[0]    , loc[1] - d),
    LEFT:  lambda loc, d: (loc[0] - d, loc[1]    )
}

nextDirection = {
    UP:    { 'L': LEFT,  'R': RIGHT },
    RIGHT: { 'L': UP,    'R': DOWN  },
    DOWN:  { 'L': RIGHT, 'R': LEFT  },
    LEFT:  { 'L': DOWN,  'R': UP    }
}

locations = [(0, 0)]
direction = UP
for d, l in data:
    direction = nextDirection[direction][d]
    locations += [move[direction](locations[-1], i) for i in range(1, l+1)]

result = [
    locations[-1],
    next(l for i, l in enumerate(locations) if l in locations[(i+1):])
]
print map(lambda x: abs(x[0]) + abs(x[1]), result)
