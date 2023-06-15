import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums = input().split()
m = int(input())
cards = input().split()

counter = Counter(nums)
for card in cards:
  print(counter[card], end=' ')