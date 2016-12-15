INPUT = [(5,4), (2,1)]
INPUT = [(13,10), (17,15), (19,17), (7,1), (5,0), (3,1)]
INPUT = [(13,10), (17,15), (19,17), (7,1), (5,0), (3,1), (11,0)]

print next(time for time in xrange(1 << 31) if all((INPUT[i][1] + i + time + 1) % INPUT[i][0] == 0 for i in range(len(INPUT))))
