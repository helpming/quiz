n = int(input())

deq = []
results = []

for i in range(n):
    ip = input()
    if ip[:10] == 'push_front':
        deq.insert(0, int(ip.split()[1]))
    elif ip[:9] == 'push_back':
        deq.append(int(ip.split()[1]))
    elif ip == 'pop_front':
        if len(deq) == 0:
            results.append(-1)
        else:
            results.append(deq.pop(0))
    elif ip == 'pop_back':
        if len(deq) == 0:
            results.append(-1)
        else:
            results.append(deq.pop())            
    elif ip == 'size':
        results.append(len(deq))
    elif ip == 'empty':
        results.append(int(len(deq) == 0))
    elif ip == 'front':
        if len(deq) == 0:
            results.append(-1)
        else:
            results.append(deq[0])
    else:
        if len(deq) == 0:
            results.append(-1)
        else:
            results.append(deq[-1])
            
for result in results:
    print(result)