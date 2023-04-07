# def solution(array, height):
#     result = 0
#     for h in array:
#         if h >= height:
#             result += 1   
#     return result

def solution(array, height):
    return len(list(filter(lambda x : x > height, array)))