def gcd(a,b):
    if b==0:
        return a
    temp=b
    b=a%b
    a=temp
    return gcd(a,b)
def lcm(a,b):
    return a*b//gcd(a,b)

if __name__ == "__main__":
    a, b = map(int, input().split())
    
    print(lcm(a,b))  
 