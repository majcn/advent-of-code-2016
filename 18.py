INPUT = '.^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^'
MAX_ROWS = 400000

def isTrap(left, right):
    return (left and not right) or (not left and right)

result = len(INPUT) * MAX_ROWS

state = map(lambda x: x == '^', INPUT)
for x in range(MAX_ROWS):
    result -= sum(state)

    prevState = [False] + state + [False]
    state = [isTrap(prevState[i], prevState[i+2]) for i in range(len(INPUT))]

print result
