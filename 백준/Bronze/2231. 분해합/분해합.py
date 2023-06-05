N = int(input())

M_list = []
for M in range(1, N):
    n_list = [M]
    for i in range(0, len(str(M))):
      n_list.append(int(str(M)[i]))
    if sum(n_list) == N:
      M_list.append(M)
if len(M_list) == 0:
  print(0)
else:
  print(min(M_list))