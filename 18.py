INPUT = '.^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^'
MAX_ROWS = 400000

def isNotTrap(left, right):
    return (left and right) or (not left and not right)

def newState(result, state):
    s = [True] + state + [True]
    newState = [isNotTrap(s[i], s[i+2]) for i in range(len(INPUT))]
    return (result + sum(newState), newState)

state = map(lambda x: x == '.', INPUT)
print reduce(lambda prevState, _: newState(*prevState), range(MAX_ROWS-1), (sum(state), state))[0]
