n = int(input())

nums = list(map(int, input().split()))

result = []

stack = []

for i in range(n):
    while stack and nums[i] > nums[stack[-1]]:
        result[stack.pop()] = nums[i]
    stack.append(i)
    result.append(-1)

for r in result:
    print(r, end=' ')