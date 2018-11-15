# Uses python3
def fib_sum_squares(n):
    lastDigits = fib_last_sequence()
    
    residualN = n % 60
    residualN1 = (n - 1) % 60
    
    result = lastDigits[residualN] * (lastDigits[residualN] + lastDigits[residualN1])
    
    return result % 10

def fib_last_sequence():
    lastDigits = [0, 1]
    
    previous = 0
    current = 1
    for i in range(2, 60):
        result = (current + previous) % 10
        previous = current
        current = result
        lastDigits.append(result)
    
    return lastDigits
    
    
if __name__ == '__main__':
    n = int(input())
    print(fib_sum_squares(n))
