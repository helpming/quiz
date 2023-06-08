p, q = map(int, input().split(' '))

for d in range(min(p, q), 0, -1):
  if p%d == 0 and q%d == 0:
    print(d)
    break

for m in range(max(p, q), p*q+1, max(p, q)):
  if m%p == 0 and m%q == 0:
    print(m)
    break 