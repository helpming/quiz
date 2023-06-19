import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

que = []
results = []

for i in range(n):
    ip = input().rstrip()
    if ip[:4] == 'push':
        que.append(int(ip.split()[1]))
    elif ip == 'pop':
        if len(que) == 0:
            results.append(-1)
        else:
            results.append(que.pop(0))
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
    print(str(result)+'\n')