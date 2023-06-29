def solution(s):
    
    stack = []
    
    for char in s:
        stack.append(char)
    
        if len(stack) >= 2 and ''.join(stack[-2:]) == '()':
            del stack[-2:]
    
    if len(stack) == 0:
        return True
    else:
        return False