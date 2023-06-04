answer = 0
n = int(input())
for p in [int(i) for i in input().split(' ')]:
    if p == 1:
        answer += 1
    else:
        for q in range(2, p):
            if p % q != 0:
                pass
            else:
                answer += 1
                break
print(n - answer)