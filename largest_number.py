#Uses python3

import sys

def largest_number(digits):
    res = ""
    while digits:
        maxDigit = 0
        
        for digit in digits:
            if is_greater(digit, maxDigit):
                maxDigit = digit
                
        res += str(maxDigit)
        digits.remove(maxDigit)        
            
    return res

def is_greater(first, second):
    
    if second == 0:
        return True
    
    if not first or not second:
        return False
    
    if first == second:
        return True
    
    first = str(first)
    second = str(second)
    
    a = first + second
    b = second + first
    
    return a > b

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
#    data = list(map(int, input().split()))
    a = data[1:]
    print(largest_number(a))
    
