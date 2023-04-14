import re

def solution(my_string):
    # return my_string.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
    return re.sub(r'[aeiou]', '', my_string)