import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for i in range(N)]
numbers.sort()

for j in numbers:
  print(j)