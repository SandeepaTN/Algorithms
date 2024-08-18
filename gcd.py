def gcd(a,b):
    if b==0:
        return a
    temp=b
    b=a%b
    a=temp
    return gcd(a,b)

if __name__ == "__main__":
    a, b = map(int, input().split())
    
    if a>b:
        print(gcd(a,b))
    else:
        print(gcd(b,a))