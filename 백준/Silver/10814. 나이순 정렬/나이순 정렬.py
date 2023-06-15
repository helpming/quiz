n = int(input())
users = []
for i in range(n):
    users.append(input())

users.sort(key=lambda x: int(x.split()[0]))

for user in users:
    print(user)