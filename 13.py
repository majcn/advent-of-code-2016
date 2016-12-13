START  = (1,1)
INPUT  = 1362
GOAL   = (31,39)
GOAL_2 = 50

cache = set()

RESULT = [None, None]

def isWall(x, y):
    magicNumber = x*x + 3*x + 2*x*y + y + y*y + INPUT
    return (len([1 for b in '{0:b}'.format(magicNumber) if b == '1']) % 2) == 1

def nextUp(x, y):
    if y == 0:
        return None

    nl = (x, y - 1)
    return None if isWall(*nl) else nl

def nextLeft(x, y):
    if x == 0:
        return None

    nl = (x - 1, y)
    return None if isWall(*nl) else nl

def nextDown(x, y):
    nl = (x, y + 1)
    return None if isWall(*nl) else nl

def nextRight(x, y):
    nl = (x + 1, y)
    return None if isWall(*nl) else nl


def checkLocationAndReturnLocation(it, l):
    if it == GOAL_2:
        RESULT[1] = len(cache)
    if l == GOAL:
        RESULT[0] = it

    return RESULT[0] != None and RESULT[1] != None

def flattenListIgnoreCache(l):
    global cache

    r = {item for sublist in l for item in sublist if item not in cache}
    cache |= r

    return r

options = [START]
it = 0
while not any(checkLocationAndReturnLocation(it, o) for o in options):
    options = flattenListIgnoreCache(filter(None, map(lambda f: f(x,y), [nextUp, nextLeft, nextRight, nextDown])) for x,y in options)
    it += 1

print RESULT
