
def fibonacci_huge(n):
    
    n=n%60  
    if n <= 1:
        return n
    last = 0
    fib = 1 
    sum=1 
    
    
    for _ in range(2, n+1):
        
        last, fib = fib, (last + fib) % 10
        sum=sum+fib
    return sum%10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_huge(n))

