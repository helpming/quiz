N, M = map(int, input().split(' '))

cards = [int(i) for i in input().split(' ')]

sums = []

for i in range(0, N-2):
  for j in range(i+1, N-1):
    for k in range(j+1, N):
      if cards[i] + cards[j] + cards[k] <= M:
        sums.append(cards[i] + cards[j] + cards[k])

print(max(sums))