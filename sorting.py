# Uses python3
#import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    k = l 
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
            if a[j] < x:
                k += 1
                a[j], a[k] = a[k], a[j]            
                
    a[l], a[k] = a[k], a[l]
    return k, j

def randomized_quick_sort3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort3(a, l, m1 - 1);
    randomized_quick_sort3(a, m2 + 1, r);

if __name__ == '__main__':
#    input = sys.stdin.read()
#    n, *a = list(map(int, input.split()))
    n, *a = list(map(int, input().split()))
    randomized_quick_sort3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
