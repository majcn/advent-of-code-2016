INPUT = 'ahsbgdzn'
STRETCH_POWER = 2016

import md5
i = 0
key = 0

possibleDuplicates = frozenset(t*3 for t in '0123456789abcdef')

def generateHash(code):
    return reduce(lambda x,y: md5.new(x).hexdigest(), range(STRETCH_POWER), md5.new(code).hexdigest())

while True:
    mh = generateHash(INPUT + str(i))
    d = next((mh[x] for x in range(30) if mh[x:x+3] in possibleDuplicates), None)
    key += any(d*5 in h for h in (generateHash(INPUT + str(x)) for x in range(i+1, i+1001))) if d else 0

    if key == 64:
    	print i
        break
    i += 1
