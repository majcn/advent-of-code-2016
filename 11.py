import itertools
import heapq
import copy
from collections import deque

floor = 0
data = [
    set(['M1', 'M2']),
    set(['G1']),
    set(['G2']),
    set([])
]

data = [
    set(['G1', 'M1', 'G6', 'M6', 'G7', 'M7']),
    set(['G2', 'G3', 'G4', 'G5']),
    set(['M2', 'M3', 'M4', 'M5']),
    set([])
]

checkedItems = set()
def serialize(floor, grid):
    return str(floor) + '#' + ';'.join(''.join(sorted(r)) for r in grid)

def isValid(grid_row):
    generators = set(x[1] for x in grid_row if x[0] == 'G')
    chips      = set(x[1] for x in grid_row if x[0] == 'M')

    return len(generators) == 0 or all([c in generators for c in chips])

def generateup(floor, grid, movedItems):
    if floor == 3:
        return None

    cf = grid[floor] - movedItems
    if not isValid(cf):
        return None
    uf = grid[floor + 1] | movedItems
    if not isValid(uf):
        return None

    up = copy.deepcopy(grid)
    up[floor] = cf
    up[floor + 1] = uf
    return up

def generatedown(floor, grid, movedItems):
    if floor == 0:
        return None

    cf = grid[floor] - movedItems
    if not isValid(cf):
        return None
    df = grid[floor - 1] | movedItems
    if not isValid(df):
        return None

    down = copy.deepcopy(grid)
    down[floor] = cf
    down[floor - 1] = df
    return down

def next(it, floor, grid):
    global checkedItems

    ss = serialize(floor, grid)
    if ss in checkedItems:
        return []
    checkedItems.add(ss)

    combinations = itertools.combinations(set([None]) | grid[floor], 2)
    nextValidGrids = []
    for c in combinations:
        cc = set(filter(None, c))
        up = generateup(floor, grid, cc)
        if up:
            # sup = serialize(floor + 1, up)
            # if sup not in checkedItems:
                # checkedItems.append(sup)
            nextValidGrids.append((it + 1, floor + 1, up))
        down = generatedown(floor, grid, cc)
        if down:
            # sdown = serialize(floor - 1, down)
            # if sdown not in checkedItems:
                # checkedItems.append(sdown)
            nextValidGrids.append((it + 1, floor - 1, down))

    return nextValidGrids

g = deque([(0, 0, data)])
while True:
# for i in xrange(10000000):
    item = g.popleft()
    if len(item[2][3]) == 14:
        print "YUHU: " + str(item[0])
        break
    # print checkedItems
    g += next(*item)
    # print g

print "DONE"






# def filterValid(s):
#     generators = set(x[1] for x in s if x[0] == 'G')
#     chips      = set(x[1] for x in s if x[0] == 'M')

#     # print chips
#     # print generators
#     return all([c in generators for c in chips])

# def checkUp(grid, floor, combinations):
#     if floor >= 3:
#         return []

#     # print list(combinations)
#     # print grid
#     # print floor
#     # print grid[floor + 1]
#     # print filter(None, combinations[0])
#     ns = []
#     for c in combinations:
#         ns.append(grid[floor + 1] + filter(None, list(c)))

#     # ns = [[i for sub in [grid[floor + 1], filter(None, c)] for i in sub] for c in combinations]
#     ns = filter(filterValid, ns)
#     # print ns
#     return ns

# def checkDown(grid, floor, combinations):
#     if floor <= 0:
#         return []

#     # print floor

#     ns = []
#     for c in combinations:
#         ns.append(grid[floor - 1] + filter(None, list(c)))
#     # ns = [[i for sub in [grid[floor - 1], filter(None, c)] for i in sub] for c in combinations]
#     ns = filter(filterValid, ns)
#     # print ns

#     return ns

# def generateGrid(grid, floor, states, isUp):
#     r = copy.deepcopy(grid)

#     if isUp:
#         r[floor + 1] = states
#         rr = r[floor]
#         for s in states:
#             if s in rr:
#                 rr.remove(s)
#     else:
#         r[floor - 1] = states
#         rr = r[floor]
#         for s in states:
#             if s in rr:
#                 rr.remove(s)

#     return r

# def getNext(it, floor, grid):
#     combinations = [(None, None)] + list(itertools.combinations([None] + grid[floor], 2))
#     upStates = checkUp(grid, floor, combinations)
#     downStates = checkDown(grid, floor, combinations)

#     # print upStates
#     # print downStates
#     u = map(lambda x: (it + 1, floor + 1, generateGrid(grid, floor, x, True )), upStates)
#     d = map(lambda x: (it + 1, floor - 1, generateGrid(grid, floor, x, False)), downStates)
#     # print u + d
#     return u + d

# paths = getNext(0, 0, data)
# # result = {0: data}
# for i in range(190000):
#     # print paths

#     el = paths.pop(0)
#     # result[el[0]] = (el[1], el[2])
#     if len(el[2][3]) == 10:
#         print el[0]
#         break
#     paths += getNext(*el)
#     # for s in getNextStates()
#     # combinations = itertools.combinations([None] + data[E], 2)
#     # upStates = checkUp(E, combinations)
#     # downStates = checkDown(E, combinations)

#     # for s in getNextStates(E):

#     # heapq.heappush(paths, (i, ))
# # print result
# # combinations = itertools.combinations([None] + data[E], 2)
# # upStates = checkUp(E, combinations)

# # E = 1
# # data[E] = upStates[0]
# # combinations = itertools.combinations([None] + data[E], 2)
# # upStates = checkUp(E, combinations)


# # print combinations