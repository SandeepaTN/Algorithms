import sys
sys.set_int_max_str_digits(65000)
def fib(n):
    if(n<=1):
        return n
    else:
        return fib(n-1)+fib(n-2)

def fibo(n):
    fib=[0,1]
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    return fib

if __name__=='__main__':

    n=int(input("Enter n:"))
    
    fibi=fibo(n)
    print(fibi[n-1])
    for _ in range(n):
        print(_,end=" ")
        print(fibi[_])
    print("hi")    
    #print(fib(n))
    
