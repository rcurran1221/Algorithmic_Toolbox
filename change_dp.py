# Uses python3
import sys

def get_change(m):
    coins = [1, 3, 4]
    return get_change_inner(m, coins)

def get_change_inner(m, coins):
    total = [sys.maxsize for i in range(m+1)]
    
    total[0] = 0
        
    results = [-1 for i in range(m+1)]
    
    for i in range(len(coins)):
        for j in range(1, len(total)):
            if coins[i] <= j:
                total[j] = min(total[j], 1 + total[j - coins[i]])
                results[j] = coins[i]
                
    return total[m]
    
if __name__ == '__main__':
#    m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
