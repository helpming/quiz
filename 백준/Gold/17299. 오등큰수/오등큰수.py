from collections import Counter

n = int(input())
nums = list(map(int, input().split()))

frequency = Counter(nums)

stack = []
result = []

for i in range(n):
    while stack and frequency[nums[i]] > frequency[nums[stack[-1]]]:
        result[stack.pop()] = nums[i]
    stack.append(i)
    result.append(-1)

for i in result:
    print(i, end=' ')