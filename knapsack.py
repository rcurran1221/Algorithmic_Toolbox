# Uses python3
import sys

def optimal_weight(W, bars):
    bars.insert(0, 0)
    n = len(bars)
    r = [[0 for y in range(n)] for x in range(W+1)]

    for b in range(1, n):
        for w in range(1, W+1):    
            r[w][b] = r[w][b-1]
            if bars[b] <= w:
                val = r[w - bars[b]][b-1] + bars[b]
                if r[w][b] < val:
                    r[w][b] = val
    
    return r[W][n-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *bars = list(map(int, input.split()))
    print(optimal_weight(W, bars))
