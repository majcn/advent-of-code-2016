# copied from wiki
# import math
# josephusProblem = lambda n: return 2 * (n - pow(2, int(math.log(n, 2)))) + 1

INPUT = 3014603
elfs = range(1, INPUT + 1)

r = 0
for i in elfs:
    r = (r + 2) % i
print r + 1

def rob(elfs):
    l = len(elfs)
    robbed = set()

    for i in xrange(l):
        r1 = ((l - i) / 2) + (2 * i)
        if r1 >= l:
            fp = elfs[:i]
            lp = [x for index, x in enumerate(elfs[i:]) if index + i not in robbed]
            return lp + fp
        robbed.add(r1)

while len(elfs) > 1:
    elfs = rob(elfs)
print elfs[0]
