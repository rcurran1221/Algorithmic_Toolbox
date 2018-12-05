# Uses python3

def edit_distance(s, t):    
    d = [[0 for i in range(len(t))] for z in range(len(s))]
    d[0] = [i for i in range(len(t))]
    
    for i in range(1, len(s)):
        d[i][0] = i
        
    for j in range(1, len(t)):
        for i in range(1, len(s)):
            insertion = d[i][j-1] + 1
            deletion = d[i -1][j] + 1
            match = d[i-1][j-1]
            mismatch = d[i-1][j-1] + 1
            if s[i] == t[j]:
                d[i][j] = min(insertion, deletion, match)
            else:
                d[i][j] = min(insertion, deletion, mismatch)            
                    
    return d[len(s)-1][len(t)-1]

if __name__ == "__main__":
    print(edit_distance(" " +input(), " " +input()))
