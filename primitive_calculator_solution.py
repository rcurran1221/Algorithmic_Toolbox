# Uses python3

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def optimal_sequence_dp(n):
    if n ==1:
        return [1]
    if n == 2:
        return [1, 2]
    
    min_count = [0 for i in range(n+1)]
    min_count[2] = 1
    min_count[3] = 1
    
    func_used = [[] for i in range(n+1)]
    func_used[1] = [lambda n: n]
    func_used[2] = [lambda n: n + 1]
    func_used[3] = [lambda n: n*3]
    
    for i in range(4, n+1):
        options = [(min_count[i-1] + 1, lambda n: n+1, lambda n: n -1)]
        if i % 2 == 0:
            options.append((min_count[i//2] + 1, lambda n: 2*n, lambda n: n//2))
        if i % 3 == 0:
            options.append((min_count[i//3] + 1, lambda n: 3*n, lambda n: n//3))

        options.sort(key = lambda a : a[0])
        min_option = options[0]
        
        prev_value = min_option[2](i)
        recent_func = min_option[1]
        
        all_funcs = func_used[prev_value][:]
        all_funcs.append(recent_func)
        
        func_used[i] = all_funcs
        min_count[i] = min_option[0]
        
    results = [1]
    min_funcs = func_used[n]
    for i in range(len(min_funcs)):
        results.append(min_funcs[i](results[i]))
    
    return results

if __name__ == '__main__':
#    input = sys.stdin.read()
#    n = int(input)
    n = int(input())
    sequence = list(optimal_sequence_dp(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
