n = int(input())

stack = []
results = []

for i in range(n):
    ip = input().rstrip()
    if ip[:4] == 'push':
        stack.append(int(ip.split()[1]))
    elif ip == 'pop':
        if len(stack) == 0:
            results.append(-1)
        else:
            results.append(stack.pop())
    elif ip == 'size':
        results.append(len(stack))
    elif ip == 'empty':
        if len(stack) == 0:
            results.append(1)
        else:
            results.append(0)
    else:
        if len(stack) == 0:
            results.append(-1)
        else:
            results.append(stack[-1])
            
for result in results:
    print(result)