# Uses python3
import sys

def binary_search(a, x):
    low, high = 0, len(a) - 1
    
    return binary_search_inner(a, low, high, x)

def binary_search_inner(a, low, high, x):
    if low > high:
        return -1
    
    mid = low + (high - low) // 2
    midValue = a[mid]
    
    if x == midValue:
        return mid
    if x < midValue:
        return binary_search_inner(a, low, mid - 1, x)
    if x > midValue:
        return binary_search_inner(a, mid + 1, high, x)
    
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))
    data = list(map(int, input().split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
#        print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end = ' ')
