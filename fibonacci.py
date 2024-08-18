def fibonacci_number(n):
    if n<=1:
        return n
    last=0
    fib=1
    for i in range(2,n+1):
        temp=fib
        fib=fib+last
        last=temp
    return fib
    

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
