INPUT = 'rrrbmfta'
gridSize = 4

import md5

def newPaths(option):
    location, code = option
    isUp, isDown, isLeft, isRight = map(lambda x: x > 'a', md5.new(code).hexdigest()[:4])

    result = []
    if isUp and location[1] > 0:
        result.append(((location[0], location[1] - 1), code + 'U'))
    if isDown and location[1] < gridSize - 1:
        result.append(((location[0], location[1] + 1), code + 'D'))
    if isLeft and location[0] > 0:
        result.append(((location[0] - 1, location[1]), code + 'L'))
    if isRight and location[0] < gridSize - 1:
        result.append(((location[0] + 1, location[1]), code + 'R'))
    return result

result = []
def filterAndSetResult(option, it):
    global result

    if option[0] == (gridSize - 1,gridSize - 1):
        if not result:
            result = [option[1].replace(INPUT, ''), it]
        else:
            result[1] = it
        return False
    return True

it = 0
options = [((0,0), INPUT)]
while options:
    it += 1
    options = filter(lambda f: filterAndSetResult(f, it), reduce(lambda res, option: res + newPaths(option), options, []))
print result
