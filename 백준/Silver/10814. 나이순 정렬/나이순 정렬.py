import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
users = []
for i in range(n):
    users.append(input().rstrip())

users.sort(key=lambda x: int(x.split()[0]))

for u in users:
    print(u+'\n')