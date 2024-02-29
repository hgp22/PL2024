import re
import sys

stack = []
b = False

try:
    for line in sys.stdin:
        words = line.split()
        for i in words:
            if b == True and re.match(r'\b\d+\b', i):
                stack.append(int(i))
            if(re.match(r'on', i, re.IGNORECASE)):
                b = True
            if(re.match(r'off', i, re.IGNORECASE)):
                b = False
            if(re.match(r'=', i, re.IGNORECASE)):
                sys.stdout.write(str(sum(stack))+'\n')
                stack.clear()

except EOFError:
    pass    
