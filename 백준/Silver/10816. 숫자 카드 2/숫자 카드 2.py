import sys
from collections import Counter

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
nums = input().split()
m = int(input())
cards = input().split()

counter = Counter(nums)
for card in cards:
  print(str(counter[card]) + ' ')
print('\n')