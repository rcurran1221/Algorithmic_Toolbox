# Uses python3
import sys
import itertools

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

def partition_opt(A):
    n = len(A)
    if n < 3:
        return 0
    
    total = sum(A[i] for i in range(n))
    if total % 3 != 0:
        return 0
    
    third = total//3
    
    P = [[None for y in range(third + 1)] for x in range(n +1)]
    for i in range(n+1):
        P[i][0] = True
    for i in range(1, third + 1):
        P[0][i] = False
        
    A.insert(0, 0)
    for i in range(1, third +1):
        for j in range(1, n+1):
            if i - A[j] >= 0:
                P[j][i] = P[j-1][i] or P[j-1][i - A[j]]
            else:
                P[j][i] = P[j-1][i]
    
    if P[n][third]:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition_opt(A))

