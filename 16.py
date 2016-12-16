import re

initialState = '10111100110001111'
diskLength = 35651584


state = initialState
while len(state) < diskLength:
    a = state
    b = state[::-1].replace('0', '2').replace('1', '0').replace('2', '1')
    state = a + '0' + b
state = state[:diskLength]


checksum = state
while len(checksum) % 2 == 0:
    checksum = ''.join(map(lambda x: '1' if x[0] == x[1] else '0', re.findall('..', checksum)))


print checksum
