# Uses python3
count = 0

def merge_sort(a):
    if len(a) == 1:
        return a
        
    m = len(a) // 2
    
    b = merge_sort(a[:m])
    c = merge_sort(a[m:])
    
    return merge(b, c)
    
def merge(b, c):
    d = []
    
    while b and c:
        if b[0] <= c[0]:
            d.append(b[0])
            del b[0]
        else:
            d.append(c[0])
            del c[0]
            increment_count(len(b))
    
    d.extend(b)
    d.extend(c)
      
    return d

def increment_count(n):
    global count
    count = count + n
    
if __name__ == '__main__':
    a = list(map(int, input().split()))
    merge_sort(a)
    print(count)