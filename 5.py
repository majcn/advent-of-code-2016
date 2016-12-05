import sys
inputdata = sys.stdin.readline()

import md5

def md5gen(code):
    for i in xrange(sys.maxint):
        h = md5.new(code + str(i)).hexdigest()
        if h.startswith('00000'):
            yield (h[5], h[6])

def result1f(result, index, value):
    if len(result) < 8:
        return result + index

    return result

indexes = [x for x in range(8)]
def result2f(result, index, value):
    global indexes
    if index.isdigit():
        i = int(index)
        if i in indexes:
            indexes.remove(i)
            result[i] = value

    return result


result1 = ''
result2 = ['']*8
gen = md5gen(inputdata)
while indexes:
    index, value = gen.next()
    result1 = result1f(result1, index, value)
    result2 = result2f(result2, index, value)
result2 = ''.join(result2)

print result1
print result2