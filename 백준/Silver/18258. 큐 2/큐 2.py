import sys
from collections import deque

n = int(input())

que = deque()
results = []

for i in range(n):
    ip = sys.stdin.readline().rstrip()
    if ip[:4] == 'push':
        que.append(int(ip.split()[1]))
    elif ip == 'pop':
        if len(que) == 0:
            results.append(-1)
        else:
            results.append(que.popleft())
    elif ip == 'size':
        results.append(len(que))
    elif ip == 'empty':
        if len(que) == 0:
            results.append(1)
        else:
            results.append(0)
    elif ip == 'front':
        if len(que) == 0:
            results.append(-1)
        else:
            results.append(que[0])
    else:
        if len(que) == 0:
            results.append(-1)
        else:
            results.append(que[-1])
            
for result in results:
    sys.stdout.write(str(result) + '\n')