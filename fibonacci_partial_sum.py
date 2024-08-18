def fibonacci_partial_sum_naive(from_, n):
    
    n=n%60  
    from_=from_%60
    if n <= 1:
        return n
    last = 0
    fib = 1 
    sum=0 
    if from_<=1:
        sum=1
    
    for _ in range(2, n+1):
        
        last, fib = fib, (last + fib) % 10
        if _>=from_:
            sum=sum+fib
    return sum%10


if __name__ == '__main__':
    
    from_, to = map(int, input().split())    
    print(fibonacci_partial_sum_naive(from_, to))
