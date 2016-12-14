import re

import sys
inputdata = sys.stdin.readline()
# inputdata = "A(1x5)BC"

data = inputdata
# data = [x.strip() for x in inputdata.split(",")]
# data = [(x[0], int(x[1:])) for x in data]

prog = re.compile(r'\((\d*)x(\d*)\)')

def krneki(s):
    result = 0
    i = 0
    while i < len(s):
        if s[i] == '(':
            substr = s[i:]
            m = prog.search(substr)
            z, f, x, y = m.group(0), substr[len(m.group(0)):], int(m.group(1)), int(m.group(2))

            # print z, f, x, y
            # print f[:x]*y
            # print z
            result += krneki(f[:x])*y
            i += len(z) + x
            # print f[:x], x, y
        else:
            result += 1
            i += 1

        # print result
        # i += 1
    return result

print krneki(data)


# import re

# import sys
# inputdata = sys.stdin.readline()
# # inputdata = "A(1x5)BC"

# data = inputdata
# # data = [x.strip() for x in inputdata.split(",")]
# # data = [(x[0], int(x[1:])) for x in data]

# prog = re.compile(r'\((\d*)x(\d*)\)')

# result = 0
# i = 0
# while i < len(data):
#     if data[i] == '(':
#         substr = data[i:]
#         m = prog.search(substr)
#         z, f, x, y = m.group(0), substr[len(m.group(0)):], int(m.group(1)), int(m.group(2))

#         # print z, f, x, y
#         # print f[:x]*y
#         # print z
#         result += len(f[:x])*y
#         i += len(z) + x
#         # print f[:x], x, y
#     else:
#         result += 1
#         i += 1

#     # print result
#     # i += 1

# print result