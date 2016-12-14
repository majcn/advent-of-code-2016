from itertools import combinations

INPUT = [
    ['M2', 'M1'],
    ['G2'],
    ['G1'],
    []
]

# INPUT = [
#     ['G1', 'M1'],
#     ['G2', 'G3', 'G4', 'G5'],
#     ['M2', 'M3', 'M4', 'M5'],
#     []
# ]

# INPUT = [
#     ['G1', 'M1', 'G6', 'M6', 'G7', 'M7'],
#     ['G2', 'G3', 'G4', 'G5'],
#     ['M2', 'M3', 'M4', 'M5'],
#     []
# ]

NR_ITEMS = max(int(item[1:]) for row in INPUT for item in row)

SINGLE_COMBINATIONS = map(lambda x: 1 << x, range(NR_ITEMS*2))
print SINGLE_COMBINATIONS
DOUBLE_COMBINATIONS = map(sum, combinations(SINGLE_COMBINATIONS, 2))
print DOUBLE_COMBINATIONS
ALL_COMBINATIONS = DOUBLE_COMBINATIONS + SINGLE_COMBINATIONS

M_MASKS = [1 << (x*2    ) for x in range(NR_ITEMS)]
G_MASKS = [1 << (x*2 + 1) for x in range(NR_ITEMS)]
M_MASK = sum(M_MASKS)
G_MASK = sum(G_MASKS)

FLOOR_MASK = 1 << (NR_ITEMS*2)


def convertToBin(item):
    t = item[0]
    n = int(item[1:]) - 1
    return 1 << (n*2 + 1) if t == 'G' else 1 << (n*2)

START = [sum(map(convertToBin, row)) for row in INPUT]
START[0] += FLOOR_MASK
START = tuple(START)




def isValidOptionRow(row):
    gs = row & G_MASK
    if gs == 0:
        return True

    ms = row & M_MASK
    return notLogicalImplication((ms << 1), gs) == 0

def generateup(floor, option, movedItems):
    cf = option[floor] - movedItems - FLOOR_MASK
    if not isValidOptionRow(cf):
        return None

    uf = option[floor + 1] + movedItems
    if not isValidOptionRow(uf):
        return None

    if floor == 0:
        return (
            cf,
            uf + FLOOR_MASK,
            option[2],
            option[3]
        )
    if floor == 1:
        return (
            option[0],
            cf,
            uf + FLOOR_MASK,
            option[3]
        )
    if floor == 2:
        return (
            option[0],
            option[1],
            cf,
            uf + FLOOR_MASK
        )

def generatedown(floor, option, movedItems):
    cf = option[floor] - movedItems - FLOOR_MASK
    if not isValidOptionRow(cf):
        return None

    df = option[floor - 1] + movedItems
    if not isValidOptionRow(df):
        return None

    if floor == 1:
        return (
            df + FLOOR_MASK,
            cf,
            option[2],
            option[3]
        )
    if floor == 2:
        return (
            option[0],
            df + FLOOR_MASK,
            cf,
            option[3]
        )
    if floor == 3:
        return (
            option[0],
            option[1],
            df + FLOOR_MASK,
            cf
        )

def getFloor(option):
    return next(i for i,v in enumerate(option) if v & FLOOR_MASK)

def notLogicalImplication(p, q):
    return p & ~q

cache = set()
GOAL = FLOOR_MASK + FLOOR_MASK - 1
RESULT = None

def checkLocationAndReturnLocation(it, o):
    global RESULT

    RESULT = o if o[3] == GOAL else None
    return RESULT

def flattenListIgnoreCache(l):
    global cache

    r = {item for sublist in l for item in sublist if item not in cache}
    cache |= r

    return r

graph = {}
def possibleOptions(option):
    floor = getFloor(option)
    row = option[floor]
    possible_combinations = [x for x in ALL_COMBINATIONS if notLogicalImplication(x, row) == 0]

    ups   = [] if floor == 3 else filter(None, map(lambda x: generateup  (floor, option, x), possible_combinations))
    downs = [] if floor == 0 else filter(None, map(lambda x: generatedown(floor, option, x), possible_combinations))

    # global graph
    # rr = ups + downs
    # for x in rr:
    #     if x not in graph:
    #         graph[x] = option

    return ups + downs

def prettyPrint(option):
    for i, o in enumerate(reversed(option)):
        e, g5, m5, g4, m4, g3, m3, g2, m2, g1, m1 = '{0:{fill}11b}'.format(o, fill='0')
        rs = 'F' + str(4 - i)
        rs += '  E' if e  != '0' else '   '
        rs += ' G5' if g5 != '0' else '   '
        rs += ' M5' if m5 != '0' else '   '
        rs += ' G4' if g4 != '0' else '   '
        rs += ' M4' if m4 != '0' else '   '
        rs += ' G3' if g3 != '0' else '   '
        rs += ' M3' if m3 != '0' else '   '
        rs += ' G2' if g2 != '0' else '   '
        rs += ' M2' if m2 != '0' else '   '
        rs += ' G1' if g1 != '0' else '   '
        rs += ' M1' if m1 != '0' else '   '
        print rs
        # print '{0:{fill}11b}'.format(o, fill='0').replace('0', ' ').replace('1', '#')
    print

# options = [START]
# graph[START] = None
# it = 0
# while not any(checkLocationAndReturnLocation(it, o) for o in options):
#     # noptions = []
#     # for asdf in options:
#     #     po = possibleOptions(asdf)
#     #     for x in po:
#     #         if x not in graph:
#     #             graph[x] = asdf
#     #     noptions.append(po)
#     # noptions = flattenListIgnoreCache(noptions)
#     options = flattenListIgnoreCache(map(possibleOptions, options))
#     # for x in noptions:
#         # if x in graph:
#             # graph[x] = options
#     # options = noptions

#     it += 1
#     print it

# print RESULT
# print prettyPrint(RESULT)
# print prettyPrint(graph[RESULT])

# e = RESULT
# while e:
#     prettyPrint(e)
#     e = graph[e]
# print
# print it