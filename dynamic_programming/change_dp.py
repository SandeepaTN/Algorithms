
def change(money):
    n=money+1
    minNumCoins=[0]*n
    
    for m in range(1,n):
        minNumCoins[m]=99999
        for coin in [1,3,4]:
            if coin> m:
                break
            numCoins=minNumCoins[m-coin]+1
            if numCoins<minNumCoins[m]:
                minNumCoins[m]=numCoins


    return minNumCoins[money] 


if __name__ == '__main__':
    m = int(input())
    print(change(m))
