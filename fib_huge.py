def reduce_n(m):
    if m<=1:
        return m
    
    else:
        fib=[0,1]
        for i in range(2,m*m+1):
            fib.append((fib[i-1]+fib[i-2])%m)
               
            if fib[i]==1 and fib[i-1]==0:
                return i-1
def fibonacci_huge(n,m):
    n=n%reduce_n(m)  
    if n <= 1:
        return n
    last = 0
    fib = 1 
     
    
    
    for _ in range(2, n+1):
        
        last, fib = fib, (last + fib) % m
        
    return fib

if __name__ == '__main__':
    n,m = map(int,input().split())
    print(fibonacci_huge(n,m))
