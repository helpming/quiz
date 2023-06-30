from collections import deque

def solution(priorities, location):
    que = deque(priorities)
    idx = deque(range(len(priorities)))
    count = 0
    target_idx = idx[location]
    while target_idx in idx:
        if que[0] >= max(que):
            que.popleft()
            idx.popleft()
            count += 1
        else:
            que.rotate(-1)
            idx.rotate(-1)
    return count