def change(money):
    n=money//10
    money=money%10
    n+=money//5
    money=money%5
    n+=money


    return n 


if __name__ == '__main__':
    m = int(input())
    print(change(m))
