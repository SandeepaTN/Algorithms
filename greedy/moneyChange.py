def change(money):
    n=0
    while money > 0:
        if money >= 10:
            n+= money // 10
            money = money % 10
        elif money >= 5:
            n+= money // 5
            money = money % 5
        else:
            n += money
            money = 0

    return n


if __name__ == '__main__':
    m = int(input())
    print(change(m))
