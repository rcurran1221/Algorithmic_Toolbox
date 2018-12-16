# Uses python3
import sys

def evalt(a, b, op):
    a = int(a)
    b = int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False
        
def min_and_max(i , j, ops, M, m):
    min_value = sys.maxsize
    max_value = -sys.maxsize - 1
    
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], ops[k])
        b = evalt(M[i][k], m[k+1][j], ops[k])
        c = evalt(m[i][k], M[k+1][j], ops[k])
        d = evalt(m[i][k], m[k+1][j], ops[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    
    return min_value, max_value

def get_maximum_value(dataset):
    d, ops = get_digits_and_operators(dataset)
    
    n = len(d)
    
    m = [[sys.maxsize for y in range(n)] for x in range(n)]
    M =[[-sys.maxsize -1 for y in range(n)] for x in range(n)]
    
    for i in range(n):
        m[i][i] = d[i]
        M[i][i] = d[i]
        
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j, ops, M, m)
    
    return M[0][n-1]

def get_digits_and_operators(dataset):
    d = []
    ops = []
    
    for i in range(len(dataset)):
        if i % 2 == 0:
            d.append(dataset[i])
        else:
            ops.append(dataset[i])
            
    return d, ops

if __name__ == "__main__":
    print(get_maximum_value(input()))
